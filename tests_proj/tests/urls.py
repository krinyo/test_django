from . import views
from django.urls import path

urlpatterns = [
    path('', views.start, name='start'),
    path('categories', views.categories, name='categories'),
    path('category/<int:category_id>', views.category_tests, name='category_tests'),
    path('tests/<int:test_id>', views.test, name="test"),
    path('tests/<int:test_id>/questions/<int:question_id>', views.question, name="question")
]