from django.urls import path
from . import views

urlpatterns = [
    path('piglatintranslator/', views.piglatintranslator, name='piglatintranslator'),
    path('translate/', views.translate, name='translate'),

] 

