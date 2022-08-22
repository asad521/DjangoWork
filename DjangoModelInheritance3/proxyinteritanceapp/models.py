from django.db import models

# Create your models here.
# Proxy model example. Fields are same as of examcenter, 
# Can change ordering and other behaviour in proxy class
class ExamCenter(models.Model):
    cname = models.CharField(default='Unknows',max_length=50)
    city = models.CharField(default='Unknows',max_length=50)
    
    
class MyCenter(ExamCenter):
    class Meta:
        proxy = True
        ordering = ['id']
        



