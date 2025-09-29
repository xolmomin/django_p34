from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, TextChoices, DateTimeField, EmailField, ForeignKey, CASCADE
from django.db.models.fields import SlugField, TextField, IntegerField, PositiveIntegerField
from django.utils.text import slugify


class User(AbstractUser):
    phone = CharField(max_length=11, unique=True)
    balance = PositiveIntegerField(default=0)


class Category(Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='categories/image/%Y/%m/%d')
    slug = SlugField(unique=True)
    background_color = CharField(max_length=20, default="#f5f5f5", help_text="Hex rang kodi, masalan: #ffcc00")

    def save(self, *, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class Advert(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)
    description = TextField()
    price = PositiveIntegerField(default=0, null=True, blank=True)
    view_count = IntegerField(default=0)
    owner = ForeignKey('apps.User', CASCADE)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    def save(self, *, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class AdvertImage(Model):
    image = ImageField(upload_to='adverts/images/%Y/%m/%d')
    advert = ForeignKey('apps.Advert', CASCADE)
