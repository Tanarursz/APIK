from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rolam/', views.rolam, name='rolam'),
    path('kapcsolat/', views.kapcsolat, name='kapcsolat'),
]


