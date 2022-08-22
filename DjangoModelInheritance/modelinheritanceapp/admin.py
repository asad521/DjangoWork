from django.contrib import admin
from .models import Student,Teacher,Contractor
# Register your models here.


@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display =  ['id','name','age','fees']
    
@admin.register(Teacher)
class Teacheradmin(admin.ModelAdmin):
    list_display =  ['id','name','age','salary','start_date']

@admin.register(Contractor)
class Contractoradmin(admin.ModelAdmin):
    list_display =  ['id','name','age','payment','start_date']