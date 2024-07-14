from django.db import models

# Create your models here.
class Products(models.Model):
    title  = models.CharField(max_length = 100, null = False)
    price  = models.DecimalField(max_digits = 10000, decimal_places = 2)
    summary = models.TextField(default = "this is summary", null = True)
