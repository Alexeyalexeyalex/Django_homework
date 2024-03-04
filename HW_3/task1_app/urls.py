from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_form, name='products_form'),
    path('products/', views.products_form, name='products_form'),
    path('products/days/<int:days>/', views.products_days_filter, name='products_days_filter'),
]