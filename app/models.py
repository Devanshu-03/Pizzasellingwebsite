from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='productimages')
    price = models.IntegerField()

    def __str__(self):
        return self.name
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)
    

    
class Signup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

    @staticmethod
    def get_customer_by_email(email=email):
        try:
         return Signup.objects.get(email=email)
        except:
            return False
        

class Order(models.Model):
    email = models.EmailField(max_length=100,default='')
    address = models.CharField(max_length=100)
    phone = models.IntegerField(default='')

    def __str__(self):
        return self.email
    




    
    


    


