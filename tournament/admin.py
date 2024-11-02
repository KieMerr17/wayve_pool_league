from django.contrib import admin
from .models import PlayerProfile, Fixture, Standings, Tournament

admin.site.register(PlayerProfile)
admin.site.register(Fixture)
admin.site.register(Standings)
admin.site.register(Tournament)
