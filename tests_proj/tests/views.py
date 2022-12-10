from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Category, Test

@login_required
def categories(request):
    all_categories = Category.objects.order_by('category_name')
    categories_count = all_categories.count()
    return render(request, 'tests/categories.html', {'all_categories' : all_categories, 
                    'categories_count' : categories_count})

def start(request):
    return redirect(categories)

@login_required
def category_tests(request, category_id):
    try:
        category_tests = Category.objects.get(id = category_id)
    except:
        raise Http404("Go fuck yourself")

    all_categories = Category.objects.order_by('category_name')
    tests_with_category = Test.objects.filter(id = category_tests.id)
    return render(request, 'tests/tests.html', {'tests_with_category' : tests_with_category})

@login_required
def test(request, test_id):
    try:
        current_test = Test.objects.get(id = test_id)
    except:
        raise Http404("Go fuck yourself")
    
    return render(request, 'tests/test.html', {'current_test' : current_test})