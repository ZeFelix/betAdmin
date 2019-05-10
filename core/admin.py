from django.contrib import admin

from .models import Event, Match, Param, Team, Tournament
# Register your models here.

admin.site.register(Event)
admin.site.register(Param)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('global_team_id', 'name')

admin.site.register(Team, TeamAdmin)
admin.site.register(Tournament)



