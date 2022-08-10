
from django.contrib import admin
from django.urls import path
from sessionapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setSession/', views.setSession),
    path('getSession/', views.getSession),
    path('delSession/', views.delSession),
   
]
