from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet,CategoryViewSet

router=DefaultRouter()
router.register('products',ProductViewSet)
router.register('categories',CategoryViewSet)

# urlpatterns = router.urls
# This is the preferred way to include the router's URLs

urlpatterns=[
    path('',include(router.urls))
    # Additional paths can be added here if needed
    # path (products/,...)
]
