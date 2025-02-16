from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    """
    Este sinal cria automaticamente um UserProfile quando um novo User é criado.
    """
    if created:  # Apenas quando o usuário for criado, não atualizado
        UserProfile.objects.create(user=instance)
