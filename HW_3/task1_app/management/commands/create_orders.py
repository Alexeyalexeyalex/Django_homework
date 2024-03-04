from django.core.management.base import BaseCommand
from task1_app.models import Order, Product, Client
from django.utils import lorem_ipsum
from random import choice, randint


class Command(BaseCommand):
    help = "Create orders"

    def handle(self, *args, **kwargs):

        products = Product.objects.all()
        clients = Client.objects.all()

        for i in range(10):
            orders = Order(
                client = choice(clients),
                product = choice(products),
                order_sum = randint(100,10000),
                order_registration_date = f'2000-03-{randint(1,30)}',)

            orders.save()
            # self.stdout.write(f'{orders.name}')



