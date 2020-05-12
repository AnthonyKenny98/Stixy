# Generated by Django 3.0.6 on 2020-05-12 04:43
# flake8: noqa
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_accountgroup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountclass',
            options={'verbose_name_plural': 'Account Classes'},
        ),
        migrations.AlterModelOptions(
            name='accountgroup',
            options={'verbose_name_plural': 'Account Groups'},
        ),
        migrations.AlterField(
            model_name='accountgroup',
            name='account_class',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='accounting.AccountClass'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=6, unique=True)),
                ('description', models.CharField(max_length=512, null=True)),
                ('account_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.AccountGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
