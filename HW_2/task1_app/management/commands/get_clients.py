from django.core.management.base import BaseCommand
from task1_app.models import Client


class Command(BaseCommand):
    help = "Get clients"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()

        return str(clients)