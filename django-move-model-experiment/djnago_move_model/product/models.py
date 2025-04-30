# store/product/models.py
from django.db import models

from catalog.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)