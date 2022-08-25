from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, CharField, DateField, DateTimeField, DecimalField, ForeignKey, ImageField, \
    IntegerField, Model, OneToOneField, PositiveSmallIntegerField, SlugField, TextChoices, TextField


class Item(Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField()
    weight = PositiveSmallIntegerField()
    price = DecimalField(decimal_places=3, max_digits=10)


class User(AbstractUser):
    middle_name = CharField(max_length=100)
    phone = CharField(max_length=100)
    address = CharField(max_length=100)


class Reviews(Model):
    author = ForeignKey(User, on_delete=CASCADE)
    text = TextField()
    created_at = DateTimeField()
    published_at = DateTimeField()
    status = CharField(max_length=100)

    # class Status(TextChoices):
    #     ON_MODERATION = '1', 'На модерации'
    #     PUBLISHED = '2', 'Опубликован'
    #     DECLINED = '3', 'Отклонен'

