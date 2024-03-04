from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    client_registration_date = models.DateField()
    
    def __str__(self):
        return f'\n{self.name}:\n{self.email}\n{self.phone_number}\n{self.address}\n{self.client_registration_date}\n'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    product_registration_date = models.DateField()
    
    def __str__(self):
        return f'\n{self.name}\n{self.description}\n{self.price}\n{self.quantity}\n{self.product_registration_date}\n'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_sum = models.IntegerField()
    order_registration_date = models.DateField()