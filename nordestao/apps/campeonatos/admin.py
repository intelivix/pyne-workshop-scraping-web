from django.contrib import admin
from campeonatos.models import Team
from campeonatos.models import Championship
from campeonatos.models import Game
from campeonatos.models import Player
from campeonatos.models import Event


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
