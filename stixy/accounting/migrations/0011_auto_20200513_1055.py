# Generated by Django 3.0.6 on 2020-05-13 10:55
# flake8: noqa
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_auto_20200513_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='entry1',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='entry2',
        ),
        migrations.AddField(
            model_name='transaction',
            name='entries',
            field=models.ManyToManyField(null=True, related_name='transactions', to='accounting.Entry', verbose_name='entry'),
        ),
    ]