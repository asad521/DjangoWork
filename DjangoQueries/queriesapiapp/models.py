from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=15 ,default='Unknown')
    roll = models.IntegerField(unique=True, null=False ,default=0)
    city = models.CharField(max_length=20 ,default='Unknown')
    marks = models.IntegerField(default=0)
    pass_date = models.DateField()
    enroll_date = models.DateTimeField()

                           
    
    
class Teachers(models.Model):
    name = models.CharField(max_length=15 ,default='Unknown')
    emp_num = models.IntegerField(unique=True, null=False ,default=0)
    city = models.CharField(max_length=20 ,default='Unknown')
    salary = models.IntegerField(default=0)
    join_date = models.DateField()