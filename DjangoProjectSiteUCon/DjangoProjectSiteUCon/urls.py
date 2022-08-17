
from django.contrib import admin
from django.urls import path
from siteunderconstruction import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeView),
    path('about/', views.aboutView),
]
