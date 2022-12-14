from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
import logging
from .models import Category, Test, Question, Answer

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

"""@login_required
def test(request, test_id):
    try:
        current_test = Test.objects.get(id = test_id)
    except:
        raise Http404("Go fuck yourself")
    #test_qss = current_test.test_questions
    #test_qss = list(Test.objects.values_list('test_questions', flat=True))
    test_qss = Question.objects.filter(test = current_test)
    
        
    #logging.warning(type(test_qss))
    return render(request, 'tests/test.html', {'current_test' : current_test, 'test_qss' : test_qss})"""
@login_required
def test(request, test_id):
    question_number = 1
    try:
        current_test = Test.objects.get(id = test_id)
    except:
        raise Http404("Go fuck yourself")
    #test_first_question = current_test.test_questions[0]
    test_questions = list(Test.objects.values_list('test_questions', flat=True))
    test_first_question = test_questions[0]
    return redirect(question(request, test_first_question.id))

@login_required
def question(request, question_id):
    try:
        current_question = Question.objects.get(id = question_id)
    except:
        raise Http404("Go fuck yourself")
    question_text = current_question.question_text
    question_answers = list(Question.objects.values_list('question_answer', flat=True))

    return render(request, {'question_text' : question_text, 'question_answers' : question_answers})
