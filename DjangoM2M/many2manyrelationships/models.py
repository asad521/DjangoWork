from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Songs(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=30,default='UnKnown')
    song_duration = models.IntegerField(default=0)


    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])