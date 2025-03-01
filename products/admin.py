from django.contrib import admin
from .models import Product,Category
# Register your models here.
# show products in ====> admin panel then ====> py manage.py makemigration 
admin.site.register(Product)
# show Category in ====> admin panel then ====> py manage.py makemigration 
admin.site.register(Category)