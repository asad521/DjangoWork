from django.contrib import admin
from .models import Songs
# Register your models here.


@admin.register(Songs)
class SongAdmin(admin.ModelAdmin):
    list_display =['song_name','song_duration','written_by']