from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from product_catalog.forms.product import ProductForm
from product_catalog.models.product import Product


def read(request, item_type):
    if item_type == 'product':
        products = Product.objects.filter(product_type='product')
    elif item_type is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(product_type='drug')

    return render(request, "list_products.html", {'products': products})
