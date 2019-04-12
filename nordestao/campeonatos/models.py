from django.db import models


class Championship(models.Model):
    year = models.IntegerField(default=0)
    name = models.CharField(max_length=20)

def get_image_path(instance, filename):
    return os.path.join('img', str(instance.category), filename)

class Team(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    titles = models.ManyToManyField(
        Championship,
        through='Title',
        through_fields='championship',
        verbose_name='lista de titulos',
    )
    state = models.CharField(max_length=20)

class Title(models.Model):
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    first_place = models.ForeignKey(Team, on_delete=models.CASCADE)
    second_place = models.ForeignKey(Team, on_delete=models.CASCADE)


class Game(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_1')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_2')
    upvotes_t1 = models.IntegerField(default=0)
    upvotes_t2 = models.IntegerField(default=0)
    score_t1 = models.IntegerField(default=0)
    score_t2 = models.IntegerField(default=0)
    location = models.CharField(max_length=20)
    game_date = models.DateTimeField()

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Event(models.Model):
    GOAL = 'GO'
    YELLOW_CARD = 'YC'
    RED_CARD = 'RC'
    EVENT_TYPE_CHOICES = (
        (GOAL, 'Goal'),
        (YELLOW_CARD, 'Yellow Card'),
        (RED_CARD, 'Red Card'),
    )
    event_type = models.CharField(
        max_length=2,
        choices=EVENT_TYPE_CHOICES,
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    gametime = models.IntegerField()

