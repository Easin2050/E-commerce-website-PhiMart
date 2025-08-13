from rest_framework import serializers
from order.models import Cart,CartItem

class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CartItem
        fields=['id','product','quantity']

    def get_product_price(self,cart_item):
        return cart_item.product.price

class CartSeriallizer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True)
    class Meta:
        model=Cart
        fields=['id','user','items']

