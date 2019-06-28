from django.contrib import admin

from .models import Event, Match, Param, Team, Tournament
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','match','param','value','period','time','team')
    search_fields = (
        'match__global_match_id__exact',
    )
admin.site.register(Event, EventAdmin)

class ParamAdmin(admin.ModelAdmin):
    list_display = ('id','name','label')
admin.site.register(Param, ParamAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('global_team_id', 'name')
admin.site.register(Team, TeamAdmin)

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Tournament, TournamentAdmin)

class MatchAdmin(admin.ModelAdmin):
    list_display = ('id','global_match_id','home_team_fk','away_team_fk','tournament','country')
    list_display_links = ('global_match_id',)
admin.site.register(Match, MatchAdmin)



