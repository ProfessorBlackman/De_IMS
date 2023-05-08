from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from product_catalog.forms.product import ProductForm

from product_catalog.models.product import Product


def delete(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        item.delete()
        return redirect('read_products')
    return render(request, 'update_product.html', {'item': item})
