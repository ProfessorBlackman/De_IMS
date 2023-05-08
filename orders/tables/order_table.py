import django_tables2 as tables

from orders.models.order import Order


class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'order_id', "order_name", 'supplier', 'product_name', 'quantity', 'unit_price', 'cost_price', 'date_added',
            'is_fulfilled', 'date_fulfilled', 'other_info', 'date_updated')

    is_selected = tables.CheckBoxColumn()
    # is_selected = tables.Column()
