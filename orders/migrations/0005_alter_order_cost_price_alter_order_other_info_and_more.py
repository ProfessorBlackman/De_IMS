# Generated by Django 4.2 on 2023-05-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='other_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='unit_price',
            field=models.FloatField(),
        ),
    ]
