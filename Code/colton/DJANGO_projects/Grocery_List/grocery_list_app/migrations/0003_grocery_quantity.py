# Generated by Django 4.0.3 on 2022-04-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list_app', '0002_grocery_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocery',
            name='quantity',
            field=models.IntegerField(default=True),
        ),
    ]