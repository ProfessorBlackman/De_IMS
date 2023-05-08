from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from orders.forms.order import OrderForm
from orders.models.order import Order


def update_order(request, product_id):
    item = get_object_or_404(Order, id=product_id)
    form = OrderForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('read-order')
    return render(request, 'update_order.html', {'form': form})
