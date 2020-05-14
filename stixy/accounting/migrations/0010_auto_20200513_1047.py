# Generated by Django 3.0.6 on 2020-05-13 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0009_auto_20200513_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.FloatField(verbose_name='Debit Amount')),
                ('credit', models.FloatField(verbose_name='Credit Amount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='account',
            name='account_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.AccountGroup', verbose_name='Account Group'),
        ),
        migrations.AlterField(
            model_name='accountgroup',
            name='account_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.AccountClass', verbose_name='Account Class'),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Transaction Date')),
                ('description', models.TextField(verbose_name='Transaction Description')),
                ('entry1', models.OneToOneField(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_a', to='accounting.Entry', verbose_name='entry')),
                ('entry2', models.OneToOneField(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_b', to='accounting.Entry', verbose_name='entry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.Account', verbose_name='Account'),
        ),
        migrations.AddField(
            model_name='entry',
            name='sub_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.SubAccount', verbose_name='Sub-Account'),
        ),
    ]
