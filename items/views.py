from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from items.models import Item, ItemSerializer, ItemPageNumberPagination, ItemFilter, Cart, CartSerializer, CartItem, CartItemSerializer, UserSerializer, User,\
    CartItemLimitOffsetPagination, WritableCartItem, WritableCartItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status


class ItemViewset(ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ItemFilter
    ordering = ['title', 'price']


class CartViewset(ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewset(ModelViewSet):
    pagination_class = CartItemLimitOffsetPagination

    def get_queryset(self):
        if self.action in ('create', 'update', 'partial_update'):
            return CartItem.objects.all()
        else:
            return CartItem.objects.all()

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return WritableCartItemSerializer
        else:
            return CartItemSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
