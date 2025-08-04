from django.urls import path
from . import views

urlpatterns = [
    path('insert-player/', views.insert_player, name='insert-player'),
    path('get-all-players/', views.get_all_players, name='get-all-players'),
    path('get-one-player/<int:jn>/', views.get_one_player, name='get-one-player'),
    path('get-all-batsmen/', views.get_all_batsmen, name='get-all-batsmen'),
    path('get-all-bowlers/', views.get_all_bowlers, name='get-all-bowlers'),
]
