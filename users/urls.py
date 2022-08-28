from django.urls import path
from items.views import ItemViewset, UserViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('current/', UserViewset.as_view({'get': 'list'})),
    path('auth/login/', obtain_auth_token),
]
