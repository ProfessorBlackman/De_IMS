# Generated by Django 4.2 on 2023-05-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0002_alter_product_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
