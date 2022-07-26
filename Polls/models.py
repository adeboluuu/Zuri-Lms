# import numbers
# from statistics import mode
# from unicodedata import name
from django.db import models

# Create your models here.


class Question(models.Model):
    question_text= models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.question_text


class Choices(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)


