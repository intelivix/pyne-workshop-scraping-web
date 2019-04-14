from django.urls import path
from django.urls import include
from campeonatos import views

app_name = 'campeonatos'

team_url_paths = [
    path('', views.teams.team_list_view, name='team_list'),
    path('<slug:slug>/', views.teams.team_detail_view, name='team_detail')
]

player_url_paths = [
    path('', views.players.player_list_view, name='player_list'),
    path('<int:pk>/', views.players.player_detail_view, name='player_detail'),
    path('<team>/jogadores/', views.players.players_by_team_list_view,
         name='players_by_team_list')
]

urlpatterns = [
    path('times/', include(team_url_paths)),
    path('jogadores/', include(player_url_paths)),
]
