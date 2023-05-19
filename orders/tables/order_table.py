import django_tables2 as tables
from django.utils.html import format_html


from orders.models.order import Order


class OrderTable(tables.Table):
    select = tables.CheckBoxColumn(verbose_name='Select', accessor='pk', orderable=False)

    class Meta:
        model = Order
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = (
            'order_id', "order_name", 'supplier', 'product_name', 'quantity', 'unit_price', 'cost_price', 'date_added',
            'is_fulfilled', 'date_fulfilled', 'other_info', 'date_updated')

    def render_select(self, record):
        return format_html('<input type="checkbox" name="selected" value="{}" />', record.pk)
