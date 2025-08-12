from django.urls import path,include
from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet

router=SimpleRouter()
router.register('products',ProductViewSet)

urlpatterns = [
    path('products/',include('product.product_urls')),
    path('categories/',include('product.category_urls')),
]
