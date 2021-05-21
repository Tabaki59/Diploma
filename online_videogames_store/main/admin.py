from django.contrib import admin

# Register your models here.
from .models import Product, Categories, DeliveryType, Genres, Languages, Payments, Platforms, Order, OrderStatus, Favorites, Profile
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(DeliveryType)
admin.site.register(Genres)
admin.site.register(Languages)
admin.site.register(Payments)
admin.site.register(Platforms)
admin.site.register(OrderStatus)
admin.site.register(Profile)