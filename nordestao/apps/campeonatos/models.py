import os
from django.db import models
from .enums import EventTypeChoices
from .enums import StateChoices


class Championship(models.Model):
    year = models.IntegerField(default=0)
    name = models.CharField(max_length=20)


def get_image_path(instance, filename):
    return os.path.join('img', str(instance.state), filename)


class Team(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='team_icons', blank=True, null=True)
    titles = models.ManyToManyField(
        Championship, through='Title',
        through_fields=('champion', 'championship'))
    state = models.CharField(max_length=20, choices=[(s.value[0], s.value[1])
                                                     for s in StateChoices])

    def __str__(self):
        return self.name


class Title(models.Model):
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    champion = models.ForeignKey(Team, on_delete=models.CASCADE,
                                 related_name='teams_champion')
    second_place = models.ForeignKey(Team, on_delete=models.CASCADE,
                                     related_name='teams_second_place')


class Game(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE,
                               related_name='team_1')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE,
                               related_name='team_2')
    upvotes_t1 = models.IntegerField(default=0)
    upvotes_t2 = models.IntegerField(default=0)
    score_t1 = models.IntegerField(default=0)
    score_t2 = models.IntegerField(default=0)
    location = models.CharField(max_length=20)
    game_date = models.DateTimeField()


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'<Player {self.name}: pk ({self.id})>'


class Event(models.Model):

    event_type = models.CharField(max_length=2,
                                  choices=[(e.value[1], e.value[0])
                                           for e in EventTypeChoices])
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    gametime = models.IntegerField()
