from django.db import models, IntegrityError
import uuid


class Order(models.Model):
    order_name = models.CharField(max_length=1000, null=False, blank=False, unique=True)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    supplier = models.CharField(max_length=1000, null=False, blank=False)
    product_name = models.CharField(max_length=1000, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    unit_price = models.FloatField(null=False, blank=False)
    cost_price = models.FloatField(null=False, blank=False)
    date_added = models.DateField(auto_now_add=True)
    is_fulfilled = models.BooleanField(default=False)
    date_fulfilled = models.DateField(null=True, blank=True)
    other_info = models.TextField(blank=True, null=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.order_name

    def save(self, *args, **kwargs):
        while True:
            try:
                super(Order, self).save(*args, **kwargs)
                break
            except IntegrityError:
                self.id = uuid.uuid4()

    class Meta:
        ordering = ["order_id"]
