# Generated by Django 4.1.4 on 2022-12-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_questions',
            field=models.ManyToManyField(to='tests.question'),
        ),
    ]
