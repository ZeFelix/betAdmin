# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Event(models.Model):
    match = models.ForeignKey('Match', on_delete=models.CASCADE, related_name="events")
    param = models.ForeignKey('Param', on_delete=models.CASCADE, related_name="events")
    value = models.IntegerField()
    period = models.CharField(max_length=255)
    time = models.IntegerField(blank=True, null=True)
    team = models.BooleanField()

    class Meta:
        db_table = 'event'
        ordering = ['param']
        

class Match(models.Model):
    global_match_id = models.IntegerField(unique=True)
    date = models.DateTimeField()
    home_team_fk = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="home_matchs")
    away_team_fk = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="away_matchs")
    score_home_team = models.IntegerField(blank=True, null=True)
    score_away_team = models.IntegerField(blank=True, null=True)
    winner = models.CharField(max_length=255, blank=True, null=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name="matchs", blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    archived = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'match'
        ordering = ['tournament']
    
    def __str__(self):
        return str(self.global_match_id)


class Param(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    note = models.TextField()

    class Meta:
        db_table = 'param'
        ordering = ['name']

    def __str__(self):
        return self.name


class Team(models.Model):
    global_team_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'team'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tournament(models.Model):
    global_tournament_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tournament'
        ordering = ['name']

    def __str__(self):
        return self.name
