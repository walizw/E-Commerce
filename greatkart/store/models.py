from django.db import models
from category.models import Category

class Product (models.Model):
    name = models.CharField (max_length=128, unique=True)
    slug = models.SlugField (max_length=128, unique=True)
    description = models.TextField (max_length=4096, blank=True)
    price = models.DecimalField (decimal_places=2, max_digits=12)
    thumb = models.ImageField (upload_to="assets/products")
    stock = models.IntegerField ()
    is_available = models.BooleanField (default=True)
    category = models.ForeignKey (Category, on_delete=models.CASCADE)

    created_date = models.DateTimeField (auto_now_add=True)
    modified_date = models.DateTimeField (auto_now=True)

    def __str__ (self):
        return self.name