from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=15 ,default='Unknown')
    roll = models.IntegerField(unique=True, null=False ,default=0)
    city = models.CharField(max_length=20 ,default='Unknown')
    marks = models.IntegerField(default=0)
    pass_date = models.DateField()