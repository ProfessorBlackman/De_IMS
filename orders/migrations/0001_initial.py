# Generated by Django 4.2 on 2023-05-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_name', models.CharField(max_length=1000, null=False, blank=False, unique=False)),
                ('order_id', models.UUIDField(max_length=16, null=False, blank=False, unique=True, primary_key=True)),
                ('supplier', models.CharField(max_length=1000, null=False, blank=False)),
                ('product_name', models.CharField(max_length=1000, null=False, blank=False)),
                ('quantity', models.IntegerField(null=False, blank=False, default=0)),
                ('unit_price', models.FloatField(null=False, blank=False, default=00.00)),
                ('cost_price', models.FloatField(null=False, blank=False, default=00.00)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('is_fulfilled', models.BooleanField(default=False)),
                ('date_fulfilled', models.DateField(null=True, blank=True)),
                ('other_info', models.TextField(blank=True, null=True, default='None')),
                ('date_updated', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['product_id'],
            },
        ),
    ]