from django import views
from django.urls import path
from . import views

urlpatterns = [       
    path('profile/', views.profile, name='profile'),
    path('show_history/<p_id>', views.show_history, name='show_history'),
    #path('race_info/<r_id>', views.race_info, name='race_info'),    
]