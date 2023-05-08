from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from product_catalog.forms.product import ProductForm
from product_catalog.models.product import Product


def update(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('read-product')
    return render(request, 'update_product.html', {'form': form})
