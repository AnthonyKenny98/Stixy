# Generated by Django 3.0.6 on 2020-05-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_auto_20200512_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='number',
            field=models.PositiveIntegerField(unique=True, verbose_name='Bank Account Number'),
        ),
    ]
