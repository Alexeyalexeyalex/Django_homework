from django.contrib import admin

from .models import Client, Product, Order

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'client_registration_date']
    list_filter = ['client_registration_date']
    fieldsets = (('Информация о пользователе', {'fields':['name','email','phone_number','address']}),
                 ('Дата регистрации', {'fields':['client_registration_date']}),)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description', 'price', 'quantity', 'product_registration_date']
    list_filter = ['product_registration_date']
    fieldsets = (('Информация о продукте', {'fields':['name','description']}),
                 ('Дополнительная информация', {'fields':['price','quantity']}),
                 ('Дата регистрации', {'fields':['product_registration_date']}),)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'product','order_sum', 'order_registration_date']
    list_filter = ['order_registration_date']
