from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default="Created",
        max_length=7,
        choices = (
            ('A', 'Approved'),
            ('D', 'Disapproved'),
            ('C', 'Created'),
            ('P', 'Pending'),
            ('S', 'Sent'),
            ('F', 'Finished'),
        )
    )

    def __str__(self):
        return f'N {pk}'
    

class RequestItem(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=100)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promo_price = models.FloatField(default=0)
    qty = models.PositiveIntegerField()
    image = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.request}'
    