# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
         return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name + '- ₹' + str(self.price)

class Color(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=64)

    def __str__(self):
        return self.name + ' ' + self.value


class ProductCategoryColor(models.Model):
    product = models.ForeignKey(Product)
    category = models.ForeignKey(Category)
    color = models.ForeignKey(Color)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
