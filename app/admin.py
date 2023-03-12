from django.contrib import admin
from .models import Product
from .models import Signup
from .models import Order
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','image','price']

admin.site.register(Product,ProductAdmin)


class SignupAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','password']

admin.site.register(Signup,SignupAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['email','phone','address']

admin.site.register(Order,OrderAdmin)


