from django.contrib import admin

from apps import models


@admin.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass
