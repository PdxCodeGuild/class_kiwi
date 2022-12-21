# Generated by Django 4.0.3 on 2022-04-08 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('complete', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo', to='todo_app.priority')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
