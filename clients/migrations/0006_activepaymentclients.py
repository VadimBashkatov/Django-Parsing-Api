# Generated by Django 3.2.10 on 2022-10-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_delete_activepaymentclients'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivePaymentClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=500, verbose_name='Full_name')),
                ('email', models.CharField(max_length=500, verbose_name='Email')),
                ('address', models.CharField(max_length=500, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=500, verbose_name='Phone')),
                ('current_balance', models.FloatField(verbose_name='Balance')),
                ('last_payment', models.DateTimeField(verbose_name='Last payment')),
                ('reg_date', models.DateTimeField(verbose_name='Date')),
                ('lastcall_date', models.DateTimeField(verbose_name='Last call')),
                ('status', models.BooleanField(verbose_name='status')),
            ],
            options={
                'verbose_name': 'active payment client',
                'verbose_name_plural': 'active payment clients',
            },
        ),
    ]