import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_api.settings")
django.setup()


import requests
from items.models import Item, User, Reviews, CartItem, Cart


# def get_data_items():
#     response_json = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json').json()
#     for item in response_json:
#         obj_id = item['id']
#         if Item.objects.filter(id=obj_id):
#             Item.objects.filter(id=obj_id).update(
#                     title=item['title'],
#                     description=item['description'],
#                     image=item['image'],
#                     weight=item['weight_grams'],
#                     price=item['price']
#                 )
#         else:
#             Item.objects.create(
#                 title=item['title'],
#                 description=item['description'],
#                 image=item['image'],
#                 weight=item['weight_grams'],
#                 price=item['price']
#             )
#
#
# def get_data_users():
#     response_json = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json').json()
#     for item in response_json:
#         obj_id = item['id']
#         if User.objects.filter(id=obj_id):
#             User.objects.filter(id=obj_id).update(
#                     username=item['email'].partition('@')[0],
#                     password=item['password'],
#                     first_name=item['info']['name'],
#                     middle_name=item['info']['patronymic'],
#                     last_name=item['info']['surname'],
#                     email=item['email'],
#                     phone=item['contacts']['phoneNumber'],
#                     address=item['city_kladr']
#
#                 )
#         else:
#             User.objects.create(
#                 username=item['email'].partition('@')[0],
#                 password=item['password'],
#                 first_name=item['info']['name'],
#                 middle_name=item['info']['patronymic'],
#                 last_name=item['info']['surname'],
#                 email=item['email'],
#                 phone=item['contacts']['phoneNumber'],
#                 address=item['city_kladr']
#             )
#
#
# def get_data_reviews():
#     response_json = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json').json()
#     for item in response_json:
#         obj_id = item['id']
#         if Reviews.objects.filter(id=obj_id):
#             Reviews.objects.filter(id=obj_id).update(
#                     author_id=item['author'],
#                     text=item['content'],
#                     created_at=item['created_at'],
#                     published_at=item['published_at'],
#                     status=item['status']
#
#                 )
#         else:
#             Reviews.objects.create(
#                 author_id=item['author'],
#                 text=item['content'],
#                 created_at=item['created_at'],
#                 published_at=item['published_at'],
#                 status=item['status']
#             )
#
#
# get_data_items()
# get_data_users()
# get_data_reviews()

# Cart.objects.create(
#     users_id=16
# )

# CartItem.objects.create(
#     item_id=2,
#     cart_id=1,
#     quantity=1,
#     price=3000,
#
# )
