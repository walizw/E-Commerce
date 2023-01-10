from django.db import models


class Category (models.Model):
    name = models.CharField (max_length=64, unique=True)
    slug = models.CharField (max_length=32, unique=True)

    description = models.TextField (blank=True)
    thumb = models.ImageField (upload_to="assets/categories/", blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__ (self):
        return self.name
