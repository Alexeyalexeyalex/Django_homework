# Generated by Django 5.0.2 on 2024-02-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='task1_app.product'),
        ),
    ]
