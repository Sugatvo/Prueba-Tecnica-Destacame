# Generated by Django 4.0.1 on 2022-01-13 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus_backend', '0004_alter_ticket_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='bus_backend.bus'),
        ),
    ]
