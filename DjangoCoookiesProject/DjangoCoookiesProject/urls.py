
from django.contrib import admin
from django.urls import path
from cookiespp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', views.setCookies),
    path('get/', views.getCookies),
    path('del/', views.delCookies),
    path('setS/', views.setSignedCookies),
    path('getS/', views.getSignedCookies),
    path('del/', views.delSignedCookies),
]
