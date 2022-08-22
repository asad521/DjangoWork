from django.db import models

# Create your models here.
class ExamCenter(models.Model):
    ecname = models.CharField(default='Unknown', max_length=50)
    city = models.CharField(default='Unknown', max_length=50)

class Student(ExamCenter):
    name = models.CharField(default='Unknown', max_length=50)
    roll = models.IntegerField(default='Unknown')