# Generated by Django 3.2.12 on 2022-04-12 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
