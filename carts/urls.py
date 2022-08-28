from django.urls import path
from items.views import ItemViewset, CartViewset, CartItemViewset, UserViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('carts/items', CartItemViewset, basename='cart_item')
urlpatterns = router.urls

urlpatterns += [
    path('carts/', CartViewset.as_view({'get': 'list'}))
]