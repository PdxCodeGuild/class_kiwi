# Generated by Django 4.0.3 on 2022-04-09 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0009_newtask_content_type_newtask_object_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newtask',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='newtask',
            name='object_id',
        ),
        migrations.AddField(
            model_name='newtask',
            name='value',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
