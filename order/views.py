from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from order.serializers import CartSeriallizer
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from order.models import Cart
# Create your views here.

class CartViewSet(CreateModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSeriallizer
