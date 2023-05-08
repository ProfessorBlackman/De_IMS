from django.urls import path

from orders.views import (
    create_order,
    read_order,
    update_order
)

app_name = "orders"
urlpatterns = [
    path("add/", create_order.add_order, name="add-order"),
    path("update/", update_order.update_order, name="update-order"),
    path("read/", read_order.ReadOrders.as_view(), name="read-order"),
]
