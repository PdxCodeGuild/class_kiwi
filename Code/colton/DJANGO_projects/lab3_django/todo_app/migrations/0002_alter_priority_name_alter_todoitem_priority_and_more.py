# Generated by Django 4.0.3 on 2022-04-08 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(blank=True, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todoitems', to='todo_app.priority'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='text',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
