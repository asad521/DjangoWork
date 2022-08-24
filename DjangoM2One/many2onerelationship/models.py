from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# This is example of one2many relations ship.
# user can create as many post as he like
class Post(models.Model):
    # if user is deleted,all post will be deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # user cannot be deleted, untill all post are deleted
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    # If user is deleted, then post will be remain with user Null
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post_title = models.CharField(default="None", max_length=70)
    post_cat = models.CharField(default="None", max_length=70)
    post_date = models.DateField()
