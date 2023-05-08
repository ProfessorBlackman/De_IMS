from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from orders.models.order import Order
from orders.forms.order import OrderForm


def add_order(request):
    form = OrderForm
    if request.method == "POST":
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("list_orders.html")
    return render(request, 'create_order.html', {'form': form})
