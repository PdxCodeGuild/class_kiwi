# Generated by Django 4.0.3 on 2022-04-01 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list_app', '0003_grocery_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocery',
            name='date_published',
        ),
    ]
