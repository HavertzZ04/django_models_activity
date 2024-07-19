from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=80)
    brand = models.CharField(max_length=80)
    description = models.TextField() #large texts
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.product_name}"
    