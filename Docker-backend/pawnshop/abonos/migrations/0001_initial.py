# Generated by Django 3.2.9 on 2022-01-29 20:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abono', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1000000000)])),
                ('date_created', models.DateField()),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
    ]
