from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
