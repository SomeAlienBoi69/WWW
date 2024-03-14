from django.contrib import admin
from .models import Seller, Product, Client


# Register your models here.

class SellerAdmin(admin.ModelAdmin):
    list_display = ('Name',)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name','Price','Description')
class ClientAdmin(admin.ModelAdmin):
    list_display = ('Name',)


admin.site.register(Seller,SellerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Client,ClientAdmin)