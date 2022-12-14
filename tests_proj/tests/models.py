from django.db import models

# Create your models here.
class Answer(models.Model):
    answer_text = models.CharField(max_length=50)
    def __str__(self):
        return self.answer_text


class Category(models.Model):
    category_name = models.CharField(("Название категории"), max_length=50)
    category_description = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.category_name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_answer = models.ManyToManyField(Answer)
    #question_test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.question_text

class Test(models.Model):
    test_name = models.CharField(max_length=50)
    test_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    test_description = models.CharField(max_length=200, null=True)
    test_questions = models.ManyToManyField(Question)
    def __str__(self):
        return self.test_name

