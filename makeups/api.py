from ninja import NinjaAPI
from .models import Brand, Products
from typing import List
from django.shortcuts import get_object_or_404

api = NinjaAPI()

@api.get("/brands", response=List[str])
def list_brands(request):
    return [brand.name for brand in Brand.objects.all()]

@api.get("/products", response=List[str])
def list_products(request):
    return [products.name for products in Products.objects.all()]
