# Generated by Django 2.1.7 on 2019-04-14 04:27

import campeonatos.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('GO', 'Goal'), ('YC', 'Yellow Card'), ('RC', 'Red Card')], max_length=2)),
                ('gametime', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvotes_t1', models.IntegerField(default=0)),
                ('upvotes_t2', models.IntegerField(default=0)),
                ('score_t1', models.IntegerField(default=0)),
                ('score_t2', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=20)),
                ('game_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to=campeonatos.models.get_image_path)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams_champion', to='campeonatos.Team')),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonatos.Championship')),
                ('second_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams_second_place', to='campeonatos.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='titles',
            field=models.ManyToManyField(through='campeonatos.Title', to='campeonatos.Championship'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonatos.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to='campeonatos.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2', to='campeonatos.Team'),
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonatos.Game'),
        ),
        migrations.AddField(
            model_name='event',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonatos.Player'),
        ),
    ]