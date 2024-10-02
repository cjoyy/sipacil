from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)  # Rating dari 0.00 sampai 9.99
    date = models.DateTimeField(default=timezone.now)  # Tanggal produk ditambahkan
    is_avail = models.BooleanField(default=True)  # Status ketersediaan produk

    def __str__(self):
        return self.name
