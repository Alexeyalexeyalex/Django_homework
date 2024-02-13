from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_form, name='main'),
    path('main/', views.main_form, name='main'),
    path('about/', views.about, name='about'),
]