from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
def courseView(request):
    mv = cache.get('movie','has_expired')
    if mv == 'has_expired':
        cache.set('movie','The Mangji', 10)
        mv = cache.get('movie')
        return render(request, 'course.html',{'mv':mv})

# for writing same above function in single line 
# version will create new version in db
# def courseView(request):
#     # mv = cache.get_or_set('fee',4709,20)
#     mv = cache.get_or_set('fee',4709,20, version=2)
#     return render(request, 'course.html',{'mv':mv})


# for cache multiple object
# def courseView(request):
#     data= {"name":"Asad", 'roll':"101"}
#     cache.set_many(data,20)
#     mv = cache.get_many(data)
#     return render(request, 'course.html',{'mv':mv})

# for delete cache in db

# def courseView(request):
#     cache.delete('data') 
#     return render(request, 'course.html')


