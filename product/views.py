from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category

@api_view()
def view_specific_product(request,id):
    try:
        product=Product.objects.get(pk=id)
        product_dict={'id':product.id,'name':product.name,'price': product.price}
        return Response(product_dict)
    except Product.DoesNotExist:
        return Response({'Messege':'No product available'})

@api_view()
def view_category(request):
    return Response({'messages':'It is the category list'})