from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(User, CustomUserAdmin)
