from django.db import models, IntegrityError
import uuid


class Product(models.Model):
    MY_CHOICES = (
        ('gadget', 'gadget'),
        ('drug', 'drug'),
    )
    brand_name = models.CharField(max_length=1000, null=False, blank=False, unique=True)
    name = models.CharField(max_length=1000, null=False, blank=False)
    product_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    product_type = models.CharField(max_length=100, null=False, blank=False, choices=MY_CHOICES, default='drug')
    quantity_available = models.IntegerField(null=False, blank=False)
    cost_price = models.IntegerField(null=False, blank=False)
    selling_price = models.IntegerField(null=False, blank=False)
    date_added = models.DateField(auto_now_add=True)
    date_bought = models.DateField(null=True, blank=True)
    other_info = models.TextField(blank=True, null=True,  default='None')
    date_updated = models.DateField(auto_now=True)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        while True:
            try:
                super(Product, self).save(*args, **kwargs)
                break
            except IntegrityError:
                self.product_id = uuid.uuid4()

    class Meta:
        ordering = ["product_id"]
