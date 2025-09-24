from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps import models


@admin.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_premium', 'price']
    search_fields = ['name']

    actions = ["make_premium"]

    @admin.action(description="Productlarni premium qilish")
    def make_premium(self, request, queryset):
        # for product in queryset:
        #     product.is_premium = True
        #     product.save()

        queryset.update(is_premium=True)

admin.site.unregister(User)
admin.site.unregister(Group)
