from django.shortcuts import render
from .models import Students
from datetime import date ,time
from django.db.models import Avg,Sum,Min,Max,Count ,Q
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

    objs = [
    Students(name='Sonam',roll='1000',city='delhi',pass_date='1997-03-10',marks='76',enroll_date='1997-03-10 13:15:35'),
    Students(name='Kajal',roll='1001',city='Mumbai',pass_date='1998-02-03',marks='95',enroll_date='1997-03-10 13:16:35'),
    Students(name='Ajay',roll='1002',city='lahore',pass_date='1992-1-04',marks='59',enroll_date='1997-03-10 14:19:35'),
    Students(name='Sonam',roll='1003',city='delhi',pass_date='2000-12-29',marks='59',enroll_date='1997-03-10 16:14:35'),
    Students(name='Asad',roll='1004',city='karachi',pass_date='2020-09-29',marks='69',enroll_date='1997-03-10 18:13:35'),
    Students(name='Salman',roll='1006',city='lahore',pass_date='2020-08-29',marks='79',enroll_date='1997-03-10 14:25:35'),
    Students(name='ali',roll='1007',city='islamabad',pass_date='2011-08-29',marks='89',enroll_date='1997-03-10 16:15:35'),
    Students(name='hina',roll='1008',city='hyderabad',pass_date='2003-07-29',marks='88',enroll_date='1997-03-10 23:35:35'),
    Students(name='maheen',roll='1009',city='faisalabad',pass_date='2004-06-29',marks='90',enroll_date='1997-03-10 13:45:35'),
    Students(name='fida',roll='1010',city='karachi',pass_date='2006-06-29',marks='65',enroll_date='1997-03-10 11:33:35'),
    Students(name='hassan',roll='1011',city='lahore',pass_date='2006-06-29',marks='95',enroll_date='1997-03-10 10:56:35'),
    Students(name='shoib',roll='1012',city='delhi',pass_date='2006-06-29',marks='45',enroll_date='1997-03-10 09:45:35'),
    Students(name='amir',roll='1013',city='murree',pass_date='2006-06-29',marks='55',enroll_date='1997-03-10 10:25:35'),
    ]

    # students_data = Students.objects.bulk_create(objs)
    students_data = Students.objects.all()
    
    # datefieldtime queries
    students_data = Students.objects.filter(enroll_date__date=date(2022, 8, 17))
    students_data = Students.objects.filter(enroll_date__date__gt=date(2021, 4, 1))
    
    # date queries ,only years,month works in datefield
    students_data = Students.objects.filter(pass_date__year=1997)
    students_data = Students.objects.filter(pass_date__year__gt=2005)
    students_data = Students.objects.filter(pass_date__month=3)
    students_data = Students.objects.filter(pass_date__month__gt=3)
    students_data = Students.objects.filter(pass_date__day=4)
    students_data = Students.objects.filter(pass_date__day__lt=20)
    students_data = Students.objects.filter(pass_date__week=2)
    students_data = Students.objects.filter(pass_date__week__gt=2)

    students_data = Students.objects.filter(pass_date__quarter__gt=2)
    students_data = Students.objects.filter(enroll_date__time__gt=time(6,00))
    students_data = Students.objects.filter(enroll_date__minute__gt=2)
    students_data = Students.objects.filter(enroll_date__hour__gt=20)
    students_data = Students.objects.filter(enroll_date__second__gt=20)

    # students_data = Students.objects.all()


    print('Output:', students_data)
    print('===========================')
    print('SQL Query:', students_data.query)
    return render(request,'home2.html' , {'students':students_data})



def homeAggregate(request):
    students_data = Students.objects.all()
    marks_avrg =students_data.aggregate(Avg('marks'))
    marks_sum =students_data.aggregate(Sum('marks'))
    marks_min =students_data.aggregate(Min('marks'))
    marks_max =students_data.aggregate(Max('marks'))
    marks_count =students_data.aggregate(Count('marks'))
    
    # Q object
    
    students_data = Students.objects.filter(Q(id__gt=1) & Q(name='Asad'))
    students_data = Students.objects.filter(Q(id__gt=1) & ~Q(name='Asad'))
    
   
    print('Output:', students_data)
    print('===========================')
    print('SQL Query:', students_data.query)
    return render(request,'Aggegation.html' , {'students':students_data,
                                               'marks_avrg':marks_avrg,'marks_count':marks_count,'marks_min':marks_min,'marks_max':marks_max,'marks_sum':marks_sum})
