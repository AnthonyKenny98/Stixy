# Generated by Django 3.0.6 on 2020-05-12 10:16
# flake8: noqa
import accounting.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_subaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('number', models.IntegerField(unique=True, verbose_name='Bank Account Number')),
            ],
            options={
                'verbose_name': 'Bank Account',
                'verbose_name_plural': 'Bank Accounts',
            },
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterModelOptions(
            name='accountclass',
            options={'verbose_name': 'Account Class', 'verbose_name_plural': 'Account Classes'},
        ),
        migrations.AlterModelOptions(
            name='accountgroup',
            options={'verbose_name': 'Account Group', 'verbose_name_plural': 'Account Groups'},
        ),
        migrations.AlterModelOptions(
            name='subaccount',
            options={'verbose_name': 'Sub-Account', 'verbose_name_plural': 'Sub-Accounts'},
        ),
        migrations.AlterField(
            model_name='account',
            name='account_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.AccountGroup', verbose_name=accounting.models._Accounting.verbose_class_name),
        ),
        migrations.AlterField(
            model_name='account',
            name='code',
            field=models.CharField(max_length=6, unique=True, verbose_name='Account Code'),
        ),
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.CharField(max_length=512, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='accountclass',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='accountgroup',
            name='account_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.AccountClass', verbose_name=accounting.models._Accounting.verbose_class_name),
        ),
        migrations.AlterField(
            model_name='accountgroup',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='code',
            field=models.CharField(max_length=4, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='description',
            field=models.CharField(max_length=512, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
