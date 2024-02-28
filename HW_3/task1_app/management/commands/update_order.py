from django.core.management.base import BaseCommand
from task1_app.models import Order, Product



class Command(BaseCommand):
    help = "Update order by id."

    def add_arguments(self, parser):
            parser.add_argument('pk', type=int, help='Order ID')
            parser.add_argument('product', type=str, help='Product ID')
            parser.add_argument('order_sum', type=str, help='Order sum')

           

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product_id = kwargs.get('product')
        order_sum = kwargs.get('order_sum')

        product = Product.objects.filter(pk=product_id).first()

        order = Order.objects.filter(pk=pk).first()
        order.product = product
        order.order_sum = order_sum


        order.save()
        self.stdout.write(f'{order}')
