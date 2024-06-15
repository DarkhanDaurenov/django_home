from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category')
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_version', 'product')