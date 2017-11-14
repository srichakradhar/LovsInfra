# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from LovsInfra import settings
from company.models import *
from reportlab.pdfgen import canvas

def stocks(request):
    stock = {}
    stock["products"] = list(Product.objects.values_list('name', flat=True))
    stock["categories"] = list(ProductCategoryColor.objects.values_list('category__name', flat=True))
    stock["colors"] = list(ProductCategoryColor.objects.values_list('color__name', flat=True))
    return render(request, 'company/stocks.html', stock)


def get_price(request, category):
    try:
        price = Category.objects.get(name=category).price
    except Category.DoesNotExist:
        price = 0
    return HttpResponse(price)

def get_categories(request, product):
    return HttpResponse(list(ProductCategoryColor.objects.filter(product=Product.objects.get(name=product)).values('category__name')))

@csrf_exempt
def generate_invoice(request):

    # Create the PDF object, using the response object as its "file."
    # p = canvas.Canvas('company/static/media/lovsInfraInvoice.pdf')

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    # p.showPage()
    # p.save()
    # return JsonResponse({"url": settings.MEDIA_URL + 'lovsInfraInvoice.pdf'})
    return JsonResponse({"url": settings.MEDIA_URL + 'LovsInfra_Invoice.pdf'})


def business(request):
    return render(request, 'company/business.html')

def employees(request):
    return render(request, 'company/employees.html')