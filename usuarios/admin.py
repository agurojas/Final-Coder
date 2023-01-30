from django.contrib import admin

from usuarios.models import UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','city','adress','phone', 'birth_date')