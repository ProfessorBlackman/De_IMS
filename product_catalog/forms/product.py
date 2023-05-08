from django.forms import ModelForm
from product_catalog.models.product import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('product_id',)

