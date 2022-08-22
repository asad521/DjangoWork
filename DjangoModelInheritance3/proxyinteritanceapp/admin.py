from django.contrib import admin
from .models import MyCenter,ExamCenter
# Register your models here.
# Register your models here.

@admin.register(MyCenter)
class centerAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']

@admin.register(ExamCenter)
class myAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']