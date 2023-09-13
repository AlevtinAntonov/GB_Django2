from django.contrib import admin
from .models import Customer, Product, Order, CategoryProduct



@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'count', 'description']
    ordering = ['category', '-count']
    list_filter = ['added_at', 'price', 'category']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'registered_at']
    ordering = ['last_name', 'first_name']
    list_filter = ['first_name', 'registered_at']
    search_fields = ['first_name']
    search_help_text = 'Поиск по полю Имя (first_name)'
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_description']
    search_fields = ['category_description']
    search_help_text = 'Поиск по полю Описание категории (description)'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'ordered_at']
    search_fields = ['total_price']
    search_help_text = 'Поиск по полю Сумме заказа (total_price)'


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
