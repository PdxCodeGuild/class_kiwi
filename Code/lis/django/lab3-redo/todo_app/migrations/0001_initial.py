# Generated by Django 4.0.3 on 2022-04-08 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('complete', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('completed_date', models.DateTimeField(null=True)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priority', to='todo_app.priority')),
            ],
        ),
    ]
