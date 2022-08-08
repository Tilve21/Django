# Generated by Django 3.2.9 on 2022-01-29 20:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_prestado', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000000000)])),
                ('interes', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('num_meses', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(12)])),
                ('date_created', models.DateField()),
                ('num_cuotas', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('monto_a_pagar', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000000000)])),
                ('deadline', models.DateField()),
                ('status', models.BooleanField()),
                ('last_modification', models.DateField()),
                ('monto_adeudado', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000000000)])),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
        ),
    ]