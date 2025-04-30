# catalog/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

# class Product(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     # category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+')