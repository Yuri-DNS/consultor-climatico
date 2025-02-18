from django.contrib.auth.models import User
from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cidades = models.ManyToManyField(Cidade, blank=True)

    def __str__(self):
        return self.user.username


class WeatherConfig(models.Model):
    api_key = models.CharField(
        max_length=255,
        help_text="Enter your OpenWeatherMap API key here"
    )

    class Meta:
        verbose_name = "Weather Configuration"
        verbose_name_plural = "Weather Configurations"

    def __str__(self):
        return self.api_key