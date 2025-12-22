from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),        
    path('races/', views.races, name='races'),
    path('race_info/<r_id>', views.race_info, name='race_info'),
    path('pclasses/', views.pclasses, name='pclasses'),
    path('pclass_info/<p_id>', views.pclass_info, name='pclass_info'),
    path('skills/', views.skills, name='skills'),
    path('items/', views.items, name='items'), 
    path('histories/', views.histories, name='histories'), 
    path('spells/', views.spells, name='spells'), 
]