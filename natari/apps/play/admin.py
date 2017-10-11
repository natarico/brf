from django.contrib import admin
from .models import GameStats

# Register your models here.


@admin.register(GameStats)
class GameStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'health', 'points',)
