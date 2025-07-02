# Create your views here.
from django.shortcuts import render
from .models import Products
from django.forms.models import model_to_dict


def index(request, product):
    record = Products.objects.get(name=product)
    productData = model_to_dict(record)
    whatsInclude = productData["whatsInclude"].split("; ")
    return render(request, 'products/index.html', {"data" : productData, "whatsInclude":whatsInclude})
