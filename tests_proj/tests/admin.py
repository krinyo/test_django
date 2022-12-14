from django.contrib import admin

# Register your models here.
from .models import Category, Test, Question, Answer

admin.site.register(Test)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)