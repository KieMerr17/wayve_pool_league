# tournament/admin.py
from django.contrib import admin
from .models import PlayerProfile, Fixture, Tournament

admin.site.register(PlayerProfile)
admin.site.register(Fixture)
admin.site.register(Tournament)