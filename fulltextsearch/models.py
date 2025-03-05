from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=500)
    brand = models.CharField(max_length=50, default='None')
    gender = models.CharField(max_length=10)
    price = models.FloatField()
    description = models.TextField()
    color = models.CharField(max_length=10)
