from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from campeonatos.models import Team

# Create your views here.

def index(request):
    return HttpResponse("Tabela de jogos do nordestao")


class TeamListView(ListView):

    model = Team
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context