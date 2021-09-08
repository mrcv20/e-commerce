from django.db import models
from PIL import Image
import os
from django.conf import settings
from utils.resize_img import resize_image

# Create your models here

class Product(models.Model):
    name = models.CharField(max_length=100)
    description_long = models.TextField(max_length=150)
    description_short = models.TextField(max_length=150)
    image = models.ImageField(upload_to='product_img')
    slug = models.SlugField(unique=True)
    price_variation = models.FloatField()
    promo_variation_price = models.FloatField(default=0)
    tp = models.CharField(
        default = 'V',
        max_length=1,
        choices=(
            ('V', 'Variation'),
            ('D', 'Default')
        )
    )
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 500

        if self.image:
            resize_image(self.image, max_image_size)

    def __str__(self):
        return self.name

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.FloatField()
    promo_price = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.product.name