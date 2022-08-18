from django.shortcuts import render
from .models import Students,Teachers
# Create your views here.
def homepage(request):
    # students_data  = Students.objects.all()
    # print('SQL Query:', students_data.query)
    
    
    
    # students_data  = Students.objects.filter(city="Karachi")
    
    # students_data  = Students.objects.exclude(city="Karachi")
    
    
    # students_data  = Students.objects.filter(city="Karachi")

    # students_data  = Students.objects.order_by("marks")
    # students_data  = Students.objects.order_by("-marks")
    # students_data  = Students.objects.order_by("?")  
    # students_data  = Students.objects.order_by("id").reverse()
    # students_data  = Students.objects.order_by("id").reverse()[:4]
    
    # will give output object in form of dictionary
    # useful for getting columns data 
    # students_data  = Students.objects.values()
    # students_data  = Students.objects.values('name','city')
    
    # will give output object in form of tuple
    # students_data  = Students.objects.values_list()   
    # students_data  = Students.objects.values_list('name','city')
    # students_data  = Students.objects.values_list('name','city' named=True)

    # to sepcify database
    # students_data  = Students.objects.using('default')
    
    # to sepcify date. second argument is month,year,week
    students_data  = Students.objects.dates('pass_date','week')
    
    # Example of query using two DBs
    

    
    
    # shared data of columns of two DBs, columns must be same
    qs1 = Students.objects.values_list('id','name', named=True)
    qs2 = Teachers.objects.values_list('id','name', named=True)
    students_data = qs1.intersection(qs2)
    
    # unique data of  columns of two DBs, & all of qs1 columns must be same
    qs1 = Students.objects.values_list('id','name', named=True)
    qs2 = Teachers.objects.values_list('id','name', named=True)
    students_data = qs1.difference(qs2)
    
    
    # unique data of  columns of two DBs, & all of qs1 columns must be same
    qs1 = Students.objects.values_list('id','name', named=True)
    qs2 = Teachers.objects.values_list('id','name', named=True)
    students_data = qs1.difference(qs2)
 
    # and or
    students_data = Students.objects.filter(city='Karachi', id=1) 
    students_data = Students.objects.filter(city='Karachi')|Students.objects.filter(city='Lahore')  

 
    print('Output:', students_data)
    print('===========================')
    print('SQL Query:', students_data.query)
    return render(request,'home.html' , {'students':students_data})
