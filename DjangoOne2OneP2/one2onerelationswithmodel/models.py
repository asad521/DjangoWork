from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#  This app creating for 
# 2nd model is creating for 

class Page(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    page_name = models.CharField(default='Unknown',max_length=90)
    page_cat = models.CharField(default='Unknown',max_length=90)
    page_date = models.DateField()
    
class Like(Page):
    panna = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,
                                 parent_link=True)
    likes = models.IntegerField(default=0)
    
    

