from rest_framework import serializers
from order.models import Cart,CartItem

class CartSeriallizer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['id','user']

