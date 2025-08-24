from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category,Review,ProductImage
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer,ProductImageSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from product.paginations import DefaultPagination
# from rest_framework.permissions import IsAdminUser,AllowAny
from api.permissons import IsAdminOrReadOnly,FullDjangoModelPermission
from rest_framework.permissions import DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from product.permissions import IsReviewAuthOrReadOnly

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    # pagination_class=PageNumberPagination
    pagination_class=DefaultPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    # filterset_fields = ['category_id','price']
    filterset_class=ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price','updated_at']
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAdminOrReadOnly]
    permission_classes=[FullDjangoModelPermission]

class ProductImageViewSet(ModelViewSet):
    serializer_class=ProductImageSerializer
    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])

    def perform_create(self,serializer):
        serializer.save(product_id=self.kwargs['product_pk'])

class CategoryViewSet(ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    queryset=Category.objects.annotate(product_count=Count('products')).all()
    serializer_class=CategorySerializer


class ReviewViewSet(ModelViewSet):
    serializer_class=ReviewSerializer
    permission_classes=[IsReviewAuthOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self,serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
    

