from django.forms import ModelForm, TextInput, NumberInput
from django.forms.models import ModelChoiceField
from django.forms.widgets import Input, Textarea, ChoiceWidget, Select

from orders.models.order import Order


class OrderForm(ModelForm):
    # def __init__(self, *args, **kwargs): super(OrderForm, self).__init__(*args, **kwargs) self.fields[
    # 'myfield'].widget.attrs.update({'class': 'form-styling', 'style': 'display: flex;  display: flex; '
    # 'justify-content: center; ' 'align-items: center;'})

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('order_id', 'date_added', 'is_fulfilled', 'date_fulfilled', 'date_updated')
        choices = ((1, 2), (3, 4), (5, 6))
        widgets = {
            'order_name': TextInput(attrs={
                'class': "inputbox",
                'title': 'a unique name to identify this order'
            }),
            'supplier': TextInput(attrs={
                'class': "inputbox",
                'title': 'who are you buying from'
            }),
            'product_name': TextInput(attrs={
                'class': "inputbox",
                'title': 'The name of the product as is written on its packaging or as specified by the supplier'
            }),
            'quantity': NumberInput(attrs={
                'class': "inputbox",
                'title': 'how many should be bought'
            }),
            'unit_price': Input(attrs={
                'class': "inputbox",
                'title': 'cost of a single item'
            }),
            'cost_price': Input(attrs={
                'class': "inputbox",
                'title': 'total cost'
            }),
            'other_info': Textarea(attrs={
                'class': "inputbox",
                'title': 'Any other information about the order'
            }),
        }
