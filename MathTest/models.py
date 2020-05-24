from django.db import models

# Create your models here.


class MathTester(models.Model):
    grade = models.CharField(max_length=20)
    Sub = models.CharField(max_length=500)
    q_no_1 = models.CharField(max_length=1000)
    q_no_2 = models.CharField(max_length=1000)
    q_no_3 = models.CharField(max_length=1000)
    q_no_4 = models.CharField(max_length=1000)
    q_no_5 = models.CharField(max_length=1000)

class MathAnswers(models.Model):
    name = models.CharField(max_length=20)
    rollNo = models.CharField(max_length=500)
    ans_no_1 = models.CharField(max_length=1000)
    ans_no_2 = models.CharField(max_length=1000)
    ans_no_3 = models.CharField(max_length=1000)
    ans_no_4 = models.CharField(max_length=1000)
    ans_no_5 = models.CharField(max_length=1000)