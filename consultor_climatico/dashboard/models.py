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