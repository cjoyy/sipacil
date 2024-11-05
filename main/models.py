from django.db import models
import uuid
from django.contrib.auth.models import User

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)  # Rating dari 0.00 sampai 9.99
    date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
