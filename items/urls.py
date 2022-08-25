from django.urls import path
from items.views import get_item


urlpatterns = [
    path('items/<int:item_id>/', get_item, name='get_item'),
]
