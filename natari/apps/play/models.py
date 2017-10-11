from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GameStats(models.Model):
    user = models.OneToOneField(User, related_name="currentStats")
    health = models.IntegerField(default=5)
    points = models.IntegerField(default=0)
    twinkies = models.IntegerField(default=0)
    nuclear = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
