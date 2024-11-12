from django.contrib.auth.models import User
from django.db import models

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    slack_url = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Nullable for cases with no image

    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Fixture(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fixture_player1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fixture_player2')
    date = models.DateTimeField(null=True, blank=True)  # Allow null for generated fixtures
    score_player1 = models.IntegerField(null=True, blank=True)
    score_player2 = models.IntegerField(null=True, blank=True)
    round_number = models.IntegerField(default=1)  # To track knockout rounds

    def __str__(self):
        return f"{self.player1.username} vs {self.player2.username} - Round {self.round_number}"

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.name
