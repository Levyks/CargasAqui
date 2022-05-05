from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, CargoStatus, Cargo

class CustomUserAdmin(UserAdmin):    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')

class CargoAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/js/libs/jquery.maskedinput.min.js', 
            '/static/js/admin/cargo.js'
        ]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(CargoStatus)