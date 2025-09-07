# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Products, Review
from django.forms.models import model_to_dict


def index(request, product):
    record = get_object_or_404(Products, name=product)
    # record = Products.objects.get(name=product)
    productData = model_to_dict(record)
    whatsInclude = productData["whatsInclude"].split("; ")
    reviewData = Review.objects.filter(product=record)
    reviews = [model_to_dict(r) for r in reviewData]
    return render(request, 'products/index.html', {"data" : productData, "whatsInclude":whatsInclude, "reviews":reviews})

