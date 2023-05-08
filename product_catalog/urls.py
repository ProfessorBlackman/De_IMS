from django.urls import path

from product_catalog.views.create_product import add
from product_catalog.views.delete_product import delete
from product_catalog.views.read_products import read
from product_catalog.views.update_product import update

app_name = "product_catalog"
urlpatterns = [
    path("add/", add, name="add-product"),
    path("delete/<int:id>", delete, name="delete-product"),
    path("update/<int:id>", update, name="update-product"),
    path("read/<item_type>", read, {'item_type': r'(None|\w+)'}, name="read-product"),
]
