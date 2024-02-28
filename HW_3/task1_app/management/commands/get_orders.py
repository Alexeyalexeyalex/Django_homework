from django.core.management.base import BaseCommand
from task1_app.models import Order


class Command(BaseCommand):
    help = "Get orders"

    def handle(self, *args, **kwargs):
        result =[]
        orders = Order.objects.all()
        for order in orders:
            result.append(f'{order.client.name}, {order.product.name}, {order.order_sum}, {order.order_registration_date}')

        return str(result)