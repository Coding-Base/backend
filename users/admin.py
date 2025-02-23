from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Unregister the default User admin and re-register with custom fields to display details
admin.site.unregister(User)

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff')

admin.site.register(User, UserAdmin)
