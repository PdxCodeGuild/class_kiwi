# Generated by Django 4.0.4 on 2022-05-12 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_groc', '0002_item_done_alter_item_date_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app_groc.storedepartment'),
        ),
    ]
