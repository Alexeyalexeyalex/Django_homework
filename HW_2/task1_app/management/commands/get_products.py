from django.core.management.base import BaseCommand
from task1_app.models import Product



class Command(BaseCommand):
    help = "Get products"

    def handle(self, *args, **kwargs):
        products = Product.objects.all()

        return str(products)