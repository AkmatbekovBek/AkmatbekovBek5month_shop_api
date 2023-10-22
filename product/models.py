from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)



class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)



class Review(models.Model):
    text = models.TextField(null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)



