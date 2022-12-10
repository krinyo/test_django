from django.contrib import admin

# Register your models here.
from .models import Category, Test

admin.site.register(Test)
admin.site.register(Category)