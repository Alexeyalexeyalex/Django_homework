from django.core.management.base import BaseCommand
from task1_app.models import Product
from django.utils import lorem_ipsum
from random import choice, randint


class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(
                name = choice(lorem_ipsum.WORDS),
                description = " ".join(lorem_ipsum.paragraphs(5, common=False)),
                price = randint(100,1000),
                quantity = randint(0,100),
                product_registration_date = f'2000-01-{randint(1,30)}')
            
            product.save()
            self.stdout.write(f'{product.name}')

