from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.func_view, name='func_view'),
    path('class/', views.ClassView.as_view(), name='class_view'),
]
