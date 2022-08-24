from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Page(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True, limit_choices_to={'is_staff':True})

    
    # only person in cchones can creat relation to user
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True, limit_choices_to={'is_staff':True})
    # delte child page will also use data(reverse delete)
    # signal is created for this 
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True, limit_choices_to={'is_staff':True})

    # PROtECT.User will not be deleted untill its one to onerealted pages are delted
    # user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    # CASCADE, if u delete user, its subsequent one2one pages will be delted
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    page_name = models.CharField(default='Unknown',max_length=90)
    page_cat = models.CharField(default='Unknown',max_length=90)
    page_date = models.DateField()
    
    

