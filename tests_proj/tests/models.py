from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(("Название категории"), max_length=50)
    category_description = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.category_name


class Test(models.Model):
    test_name = models.CharField(max_length=50)
    test_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    test_description = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.test_name