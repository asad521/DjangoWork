from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(default='Unknown', max_length=30)
    age = models.IntegerField(default=0)
    start_date = models.DateField()
    class Meta:
        abstract =True
        
        
class Student(Person):
    # inherit all field, add new fee  property, remove start date field
    fees = models.IntegerField(default=0)
    start_date = None

    
    
class Teacher(Person):
    # inherit all field and add new salary field 
    salary = models.IntegerField(default=0)
    
class Contractor(Person):
    # inherita all fields,override start_date field and add new payment field  
    start_date = models.DateTimeField()
    payment = models.IntegerField(default=0)


# class Student(models.Model):
#     name = models.CharField(default='Unknown', max_length=30),
#     age = models.IntegerField(),
#     fee = models.IntegerField(),
#     start_date = models.DateField()

# class Teachers(models.Model):
#     name = models.CharField(default='Unknown', max_length=30),
#     age = models.IntegerField(),
#     salary = models.IntegerField(),
#     join_date = models.DateField(),
# class Contractor(models.Model):
#     name = models.CharField(default='Unknown', max_length=30),
#     age = models.IntegerField(),
#     fee = models.IntegerField(),
#     contract_date = models.DateTimeField(),
    

