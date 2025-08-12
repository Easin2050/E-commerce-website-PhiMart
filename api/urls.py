from django.urls import path,include
from product.views import ProductViewSet,CategoryViewSet, ReviewViewSet
from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('categories',CategoryViewSet)

product_router=routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-reviews')

# urlpatterns = router.urls
# This is the preferred way to include the router's URLs

urlpatterns=[
    path('',include(router.urls)),
    # Additional paths can be added here if needed
    # path (products/,...)
    path('', include(product_router.urls) )
]
