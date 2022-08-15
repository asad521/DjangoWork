from middlwarehooks import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('process/', views.exceptionView),
    path('template/', views.templateResponseView),
]
