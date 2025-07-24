from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category
from rest_framework import status
from product.serializers import ProductSerializer

@api_view()
def view_specific_product(request,id):
    product=get_object_or_404(Product,pk=id)
    serializer=ProductSerializer(product)
    return Response(serializer.data)
    
@api_view()
def view_category(request):
    return Response({'messages':'It is the category list'})