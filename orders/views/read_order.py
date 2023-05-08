from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django_tables2 import SingleTableView


from orders.models.order import Order
from orders.tables.order_table import OrderTable


# def read_orders(request):
#     orders = Order.objects.all()
#
#     return render(request, "list_orders.html", {'orders': orders})


class ReadOrders(SingleTableView):
    model = Order
    table_class = OrderTable
    template_name = 'list_orders.html'
