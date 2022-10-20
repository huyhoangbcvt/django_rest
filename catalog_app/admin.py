from django.contrib import admin
from .models.category_model import Category
from .models.product_model import Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)