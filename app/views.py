from django.shortcuts import render,redirect
from .models import Product
from .models import Signup
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from .models import Order
from django.http import HttpResponse
from app.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.contrib import messages


# Create your views here.
class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])


        return redirect('index')
        


    def get(self,request):
        product = Product.objects.all()
        
        return render(request,'index.html',{"product":product})


#signup
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        #validations
        error_message = None

        if not (first_name):
            error_message = "firstname is requried !!"
        elif len(first_name)<1:
            error_message = "firstname should be greater then 1"
        elif len(last_name)<1:
            error_message = "lastname should be greater then 1"
        elif len(email)<1:
            error_message = "email should be greater then 1"
        elif len(phone)<1:
            error_message = "phone number should be greater then 10"
        elif len(password)<1:
            error_message = "password should be greater or equal to 10"

        if not error_message:
              customer = Signup(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password)
              customer.password = make_password(customer.password)
              customer.save()
              return redirect('index')
        else:
            return render(request,'signup.html',{"error":error_message})
    return render(request,'signup.html')
#signin
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        customer = Signup.get_customer_by_email(email)
        error_message = None 
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect('index')
            else:
                error_message = "email or password is invalid !!"
            return render(request,'signin.html',{"error":error_message})
    return render(request,'signin.html')
#logout
def logout(request):
    request.session.clear()
    return redirect('index')

class Cart(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        print(products)

        return render(request,'cart.html',{'products':products})

class Checkout(View):
    
    def post(self,request):
        if request.method == 'POST':
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']

            #validation
            error_message = None
            if not (email):
              error_message = "email is required !!"
            elif len(email)<1:
              error_message = "email should be fill correctly !!"
            elif len(phone)<10:
              error_message = "phone numbe should be fill correctly"
            elif len(address)<1:
              error_message = "address should be fill correctly"

            if not error_message:
                    order = Order(email=email,address=address,phone=phone)
                    order.save()
                    messages.success(request,"Your Order has been placed successfully")
                    return redirect('index')
            else:
                    return render(request,'order.html',{"error":error_message})
        return render(request,'order.html')
    
    @method_decorator(auth_middleware) 
    def get(self,request):
        return render(request,'order.html')
    


