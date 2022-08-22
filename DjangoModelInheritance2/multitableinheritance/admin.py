from django.contrib import admin
from .models import Student,ExamCenter
# Register your models here.
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display= ['id','name','roll']
    
    
@admin.register(ExamCenter)
class Examadmin(admin.ModelAdmin):
    list_display= ['id','ecname','city']