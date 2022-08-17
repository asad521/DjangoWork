from django.contrib import admin
from .models import Students,Teachers
# Register your models here.


@admin.register(Students)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city','marks','pass_date']
    
    
@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','emp_num','city','salary','join_date']