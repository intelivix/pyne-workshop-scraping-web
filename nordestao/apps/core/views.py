from django.views.generic.list import ListView
from campeonatos.models import Team

class TeamModelMixin(object):
    model = Team

class HomePageView(TeamModelMixin, ListView):

    template_name = "index.html"
    context_object_name = 'team'


index = HomePageView.as_view()
