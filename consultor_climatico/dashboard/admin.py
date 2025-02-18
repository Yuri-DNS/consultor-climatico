from django.contrib import admin
from .models import Cidade, UserProfile, WeatherConfig
# Register your models here.

# Crie um inline para o relacionamento ManyToMany entre UserProfile e Cidade.


class CidadeInline(admin.TabularInline):
    model = UserProfile.cidades.through
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]
    list_display = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Cidade)
admin.site.register(WeatherConfig)