from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewsSet

class ProductViewSet(ModelViewsSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def destroy(self,request,*args,**kwargs):
        product=self.get_object()
        if product.stock>10:
            return Response({'message': 'Product with stock more than 10 can not be deleted'})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)


# It is used for reduce redundent code and to use the same serializer for both list and create operations.
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    '''def get_queryset(self):
        return Product.objects.select_related('category').all()
    
    def get_serializer_class(self):
        return ProductSerializer'''


class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field = 'id'

    def delete(self, request,id):
        product=get_object_or_404(Product, pk=id)
        if product.stock > 0:
            return Response({'message': 'Product with stock more than 10 can not be deleted'})
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(ListCreateAPIView):
    queryset=Category.objects.annotate(
            product_count=Count('products')).all()
    serializer_class=CategorySerializer


class ViewSpecificCategory(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.annotate(
            product_count=Count('products')).all()
    serializer_class=CategorySerializer
    lookup_field = 'id'