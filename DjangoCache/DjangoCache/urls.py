
from django.contrib import admin
from django.urls import path
from cacheapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.courseView),
]
