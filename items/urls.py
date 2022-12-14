from django.urls import path
from items.views import ItemViewset, CartViewset, CartItemViewset, UserViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('items', ItemViewset)
urlpatterns = router.urls
