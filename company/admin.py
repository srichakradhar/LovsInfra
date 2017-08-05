# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from company.models import *


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(CategoryColor)
