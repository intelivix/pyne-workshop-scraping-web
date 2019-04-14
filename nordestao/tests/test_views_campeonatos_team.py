import pytest

from django.urls import reverse
from campeonatos.views import team_list_view
from campeonatos.views import team_detail_view
from model_mommy import mommy


class TestTeamViews(object):

    @pytest.mark.django_db
    def test_team_list(self, rf):
        request = rf.get(reverse('campeonatos:team_list'))
        response = team_list_view(request)
        assert response.status_code == 200
        assert 'team/team_list.html' in [t for t in response.template_name]

    @pytest.mark.django_db
    def test_team_detail(self, rf):
        t1 = mommy.make('campeonatos.Team', name='Generic Team')
        payload = {'slug': t1.slug}
        request = rf.get(reverse('campeonatos:team_detail', kwargs=payload))
        response = team_detail_view(request, **payload)
        assert response.status_code == 200
        assert 'team/team_detail.html' in [t for t in response.template_name]
