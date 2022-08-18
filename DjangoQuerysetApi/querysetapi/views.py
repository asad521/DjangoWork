from django.shortcuts import render
from .models import Students
# Create your views here.
def homepage(request):
    students_data = Students.objects.all()
    # find exact data,case sensitive
    # students_data = Students.objects.filter(name__exact='Mani')
    # find sth contain ,case senstivie
    students_data = Students.objects.filter(name__contains='ad')
    # find sth contain ,case insenstivie
    students_data = Students.objects.filter(name__contains='ad')
    # find specifiy data based  on give
    students_data = Students.objects.filter(id__in=['4','3','9'])
    students_data = Students.objects.filter(marks__in=['88','78','55 '])
    # find based on comparision *(integer)
    students_data = Students.objects.filter(marks__gt=82)
    students_data = Students.objects.filter(marks__gte=82)
    students_data = Students.objects.filter(marks__lte=82)
    students_data = Students.objects.filter(marks__lt=82)
    
    # find based on  comparision alphabetes  
    students_data = Students.objects.filter(name__startswith='s')
    students_data = Students.objects.filter(name__istartswith='S')
    students_data = Students.objects.filter(name__endswith='D')
    # find based on range  
    students_data = Students.objects.filter(pass_date__range=('2000-01-01','2021-12-30'))
    # find based on datetime  
    # students_data = Students.objects.filter(admdatetime__date=date('2020,1,3')) 
    
    # will show if any row in columns is null or not
    students_data = Students.objects.filter(name__isnull=False)


    
    # students_data = Students.objects.all()

    print('Output:', students_data)
    print('===========================')
    print('SQL Query:', students_data.query)
    return render(request,'home2.html' , {'students':students_data})
