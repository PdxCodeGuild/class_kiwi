# Generated by Django 4.0.3 on 2022-04-08 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoPriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.BooleanField(default=False)),
            ],
        ),
    ]
