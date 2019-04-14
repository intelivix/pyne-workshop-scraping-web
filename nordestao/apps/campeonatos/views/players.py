from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from campeonatos.models import Player
from campeonatos.models import Team


class PlayerModelMixin(object):
    model = Player


class PlayerListView(PlayerModelMixin, ListView):

    paginate_by = 10
    template_name = 'player/player_list.html'
    context_object_name = 'players'


class PlayersByTeamListView(PlayerModelMixin, ListView):

    template_name = 'player/players_by_team_list.html'
    context_object_name = 'players'

    def get_queryset(self, *args, **kwargs):
        self.team = get_object_or_404(Team, slug=self.kwargs['team'])
        return super().get_queryset().filter(team=self.team)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = self.team
        return context


class PlayerDetailView(PlayerModelMixin, DetailView):

    template_name = 'player/player_detail.html'
    context_object_name = 'player'


player_list_view = PlayerListView.as_view()
player_detail_view = PlayerDetailView.as_view()
players_by_team_list_view = PlayersByTeamListView.as_view()
