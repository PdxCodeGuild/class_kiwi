# Generated by Django 4.0.3 on 2022-04-15 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_rename_text_todoitem_item_todoitem_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='todoitem',
            old_name='item',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related', to='todo_app.priority'),
        ),
    ]
