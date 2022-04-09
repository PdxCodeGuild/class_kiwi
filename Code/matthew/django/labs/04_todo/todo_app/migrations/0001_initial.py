# Generated by Django 4.0.3 on 2022-04-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=25)),
                ('complete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
