# Generated by Django 4.2 on 2023-05-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0004_alter_product_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
