from django.shortcuts import render
from .models import Students
# Create your views here.
def homepage(request):
    
    # students_data  = Students.objects.get(pk=1)
    # below give error because there are two asad
    # students_data  = Students.objects.get(name='Asad')
    
    # students_data  = Students.objects.first()
    # students_data  = Students.objects.order_by('city').first()
    # students_data  = Students.objects.last()
    
    # students_data  = Students.objects.latest('pass_date')
    # students_data  = Students.objects.earliest('pass_date')
    
    # for saving data into database
    # students_data = Students.objects.create(name='Rahul',roll='7888',
    #                 city='delhi',pass_date='1992-01-20',marks='99')
    # students_data  = Students.objects.all()
    
    
    # diretly creating data if not else get only
    # students_data = Students.objects.get_or_create(name='Rahul',roll='8888',
    #                 city='delhi',pass_date='1992-01-20',marks='99')
    # students_data  = Students.objects.all()
    
    # get city with name sindh and update city with mumbai
    # students_data = Students.objects.filter(city='Sindh').update(city='Mumbai')
    # students_data  = Students.objects.all()
    
    # it will fetch data of given id and name and update it with default
    # if data is not found, then it will create new
    # if there is other requried field, it will generate error if not given in defaults
    # students_data = Students.objects.update_or_create(id=15,name='Kabir', defaults={'name':'Kohli'})
    # students_data  = Students.objects.all()

    # creating bulk data
    # objs = [
    # Students(name='Sonam',roll='2010',city='delhi',pass_date='1997-03-10',marks='76'),
    # Students(name='Kajal',roll='2018',city='Mumbai',pass_date='1998-09-03',marks='95'),
    # Students(name='Ajay',roll='2008',city='Dakan',pass_date='1992-07-04',marks='59'),
    # Students(name='Akshay',roll='2013',city='delhi',pass_date='2000-06-29',marks='79'),
    # ]
    # students_data = Students.objects.bulk_create(objs)
    students_data = Students.objects.all()
    
    
    # bulk update or create single in single value 
    # first get all student data
    # all_students_data = Students.objects.all()
    # for student in all_students_data:
    #     student.city='Delhi'
    # Students_data = Students.objects.bulk_update(all_students_data,['city'])
    # students_data = Students.objects.all()
    
    # in_bulk will give specifed rowns on all 
    # first get all student data
    # students_data = Students.objects.in_bulk([1,3])
    # print(students_data[3].name)
    # students_data = Students.objects.all()

    # delete data
    # Students.objects.get(pk=6).delete()
    # students_data = Students.objects.all()
    
    # Students.objects.filter(name='Asad').delete()
    students_data = Students.objects.all()
    print(Students.objects.count())

    # print('Output:', students_data)
    print('===========================')
    # print('SQL Query:', students_data.query)
    return render(request,'home2.html' , {'students':students_data})
