# Generated by Django 4.0.3 on 2022-04-06 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list_app', '0007_remove_grocery_user_alter_grocery_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grocery',
            old_name='deleted',
            new_name='completed',
        ),
    ]