from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from items.models import Item
from django.http import Http404


def get_item(request: WSGIRequest, item_id: int) -> HttpResponse:
    if request.method == 'GET':
        try:
            Item.objects.get(id=item_id)
            return HttpResponse(Item.objects.filter(id=item_id).values())
        except Item.DoesNotExist:
            raise Http404

