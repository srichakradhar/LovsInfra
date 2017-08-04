# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)


class Color(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=64)


class CategoryColor(models.Model):
    category = models.ForeignKey(Category)
    color = models.ForeignKey(Color)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)