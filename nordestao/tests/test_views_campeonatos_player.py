import pytest

from django.urls import reverse
from campeonatos.views import player_list_view
from campeonatos.views import player_detail_view
from campeonatos.views import players_by_team_list_view
from model_mommy import mommy


class TestPlayerViews(object):

    @pytest.mark.django_db
    def test_player_list(self, rf):
        request = rf.get(reverse('campeonatos:player_list'))
        response = player_list_view(request)
        assert response.status_code == 200
        assert 'player/player_list.html' in [t for t in response.template_name]

    @pytest.mark.django_db
    def test_player_detail(self, rf):
        t1 = mommy.make('campeonatos.Team', name='Generic Team')
        p1 = mommy.make('campeonatos.Player', name='Generic Player',
                        team=t1)
        payload = {'pk': p1.id}
        request = rf.get(reverse('campeonatos:player_detail', kwargs=payload))
        response = player_detail_view(request, **payload)
        assert response.status_code == 200
        assert 'player/player_detail.html' in [t for t in
                                               response.template_name]
        assert 'Generic Player' in response.rendered_content
        assert 'Generic Team' in response.rendered_content

    @pytest.mark.django_db
    def test_players_by_team_list(self, rf):
        t1 = mommy.make('campeonatos.Team', name='Generic Team')
        t1.save()
        for n in range(11):
            p = mommy.make('campeonatos.Player',
                           name=f'Generic Player {n}', team=t1)
            p.save()
        payload = {'team': t1.slug}
        request = rf.get(reverse('campeonatos:players_by_team_list',
                                 kwargs=payload))
        response = players_by_team_list_view(request, **payload)
        assert response.status_code == 200
        assert 'player/players_by_team_list.html' in \
            [t for t in response.template_name]
        assert 'Generic Team' in response.rendered_content
        assert 'Generic Player 0' in response.rendered_content
        assert 'Generic Player 10' in response.rendered_content
