from django.core.management.base import BaseCommand
from task1_app.models import Client
from django.utils import lorem_ipsum
from random import choice, randint


class Command(BaseCommand):
    help = "Create clients"

    def handle(self, *args, **kwargs):
        for i in range(10):
            client_name = choice(lorem_ipsum.WORDS)
            client = Client(
                name = client_name,
                email = f'{client_name}_{i}@mail.ru',
                phone_number = f'+7(495)-{randint(111,999)}-{randint(10,99)}-{randint(10,99)}',
                address = " ".join(lorem_ipsum.paragraphs(2, common=False)),
                client_registration_date = f'2000-01-{randint(1,30)}')
            
            client.save()
            self.stdout.write(f'{client.name}')


           