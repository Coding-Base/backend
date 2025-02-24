from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import GPCalculatorUsage

User = get_user_model()

# Unregister the default registration for User if it exists.
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'gp_usage_count')

    def gp_usage_count(self, obj):
        return obj.gp_usages.count()
    gp_usage_count.short_description = "GP Calculator Uses"

admin.site.register(User, CustomUserAdmin)

class GPCalculatorUsageAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp')
    list_filter = ('user',)

admin.site.register(GPCalculatorUsage, GPCalculatorUsageAdmin)
