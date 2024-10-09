from django.urls import path
from .views import class_based_view, function_based_view

urlpatterns = [
    path('class-based/', class_based_view, name='class_based'),
    path('function-based/', function_based_view, name='function_based'),
]
