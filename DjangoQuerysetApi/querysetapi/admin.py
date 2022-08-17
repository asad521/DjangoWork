from django.contrib import admin
from .models import Students
# Register your models here.


@admin.register(Students)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city','marks','pass_date']