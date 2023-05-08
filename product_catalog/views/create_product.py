from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from product_catalog.forms.product import ProductForm
from product_catalog.models.product import Product


def add(request):
    form = ProductForm
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("list_products.html")
    return render(request, 'add_product.html', {'form': form})
