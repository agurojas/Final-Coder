from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',)
    phone = models.CharField(max_length=25, null=True, blank=True, verbose_name='Celular')
    birth_date = models.DateField(null=True, blank=True,verbose_name='Fecha de Nacimiento')
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True, verbose_name='Imagen de perfil')
    adress = models.CharField(max_length=25, null=True, blank=True, verbose_name='Direccion')
    city = models.CharField(max_length=25, null=True, blank=True, verbose_name='Ciudad')
