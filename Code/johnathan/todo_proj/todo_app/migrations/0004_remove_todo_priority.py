# Generated by Django 4.0.3 on 2022-04-09 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todo_prioritychoice_alter_priority_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='priority',
        ),
    ]