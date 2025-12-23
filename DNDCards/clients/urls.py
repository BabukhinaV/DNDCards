from django import views
from django.urls import path
from . import views

urlpatterns = [       
    path('profile/', views.profile, name='profile'),
    path('show_history/<p_id>', views.show_history, name='show_history'),
    path('delete_character/<p_id>', views.delete_character, name='delete_character'), 
    path('create_player', views.create_player, name='create_player'),  
    path('edit_player/<p_id>', views.edit_player, name='edit_player'),  
    path('distribute_points/<p_id>', views.distribute_points, name="distribute_points"),  
]