from django.urls import path
from . import views

urlpatterns = [
    path('wordcounter/', views.wordcounter, name='wordcounter'),
    path('count/', views.count, name='count'),

] 

