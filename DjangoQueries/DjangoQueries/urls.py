
from django.contrib import admin
from django.urls import path
from queriesapiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage),
]
