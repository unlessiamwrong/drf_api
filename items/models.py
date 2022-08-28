from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, ImageField, \
    Model, PositiveSmallIntegerField, TextField, ManyToManyField, PositiveIntegerField
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.serializers import ModelSerializer, Serializer, ReadOnlyField, IntegerField, SerializerMethodField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.validators import ValidationError
from rest_framework import serializers


class Item(Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField()
    weight = PositiveSmallIntegerField()
    price = models.DecimalField(decimal_places=3, max_digits=10)


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemFilter(filters.FilterSet):
    price__gt = filters.NumberFilter(field_name="price", lookup_expr='gt')
    price__gte = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price__lt = filters.NumberFilter(field_name="price", lookup_expr='lt')
    price__lte = filters.NumberFilter(field_name="price", lookup_expr='lte')
    weight__gt = filters.NumberFilter(field_name="weight", lookup_expr='gt')
    weight__gte = filters.NumberFilter(field_name="weight", lookup_expr='gte')
    weight__lt = filters.NumberFilter(field_name="weight", lookup_expr='lt')
    weight__lte = filters.NumberFilter(field_name="weight", lookup_expr='lte')

    class Meta:
        model = Item
        fields = ['price__gt', 'price__gte', 'price__lt', 'price__lte', 'weight__gt', 'weight__gte', 'weight__lt',
                  'weight__lte']


class ItemPageNumberPagination(PageNumberPagination):
    pass


class User(AbstractUser):
    middle_name = CharField(max_length=100)
    phone = CharField(max_length=100)
    address = CharField(max_length=100)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'middle_name', 'phone', 'address']
        extra_kwargs = {'username': {'required': False, 'read_only': True},
                        'middle_name': {'required': False},
                        'phone': {'required': False},
                        }


class Reviews(Model):
    author = ForeignKey(User, on_delete=CASCADE)
    text = TextField()
    created_at = DateTimeField()
    published_at = DateTimeField()
    status = CharField(max_length=100)


class CartItem(Model):
    item = models.ForeignKey('Item', on_delete=CASCADE)
    cart = models.ForeignKey('Cart', on_delete=CASCADE)
    quantity = PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0)


class CartItemSerializer(ModelSerializer):
    item = ItemSerializer(many=False, read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=3,
        source='price',
        read_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'item_id', 'quantity', 'price', 'total_price']
        extra_kwargs = {'quantity': {'required': False},
                        'price': {'required': False, 'read_only': True},
                        'cart': {'read_only': True},
                        'item': {'read_only': False}
                        }


class CartItemLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 5


class Cart(Model):
    items = ManyToManyField('CartItem', related_name='cart_items')
    user = models.ForeignKey(User, on_delete=CASCADE)


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_cost = SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_cost']

    def get_total_cost(self, instance):
        total_cost = 0
        for item in instance.items.all():
            total_cost += item.price
        return total_cost


class WritableCartItem(Model):
    item = models.ForeignKey('Item', on_delete=CASCADE)
    quantity = PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0)


class WritableCartItemSerializer(ModelSerializer):
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=3,
        source='price',
        read_only=True
    )

    class Meta:
        model = WritableCartItem
        fields = ['id', 'item', 'quantity', 'price', 'total_price']
        extra_kwargs = {'price': {'required': False, 'read_only': True},
                        'quantity': {'required': False}
                        }
