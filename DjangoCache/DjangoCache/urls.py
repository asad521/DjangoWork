
from django.contrib import admin
from django.urls import path
from cacheapp import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cache_page(30)(views.courseView)),
] 
