from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from campeonatos.models import Team


class TeamModelMixin(object):
    model = Team


class TeamListView(TeamModelMixin, ListView):

    paginate_by = 10
    template_name = 'team/team_list.html'
    context_object_name = 'teams'


class TeamDetailView(TeamModelMixin, DetailView):

    template_name = 'team/team_detail.html'
    context_object_name = 'team'


team_list_view = TeamListView.as_view()
team_detail_view = TeamDetailView.as_view()
