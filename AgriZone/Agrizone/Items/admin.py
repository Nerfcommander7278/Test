from django.contrib import admin
from .models import product

# Register your models here.
class ItemsA(admin.ModelAdmin):
    pass

admin.site.register(product, ItemsA)