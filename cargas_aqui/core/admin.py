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

    model = Cargo
    list_display = ('route', 'get_state', 'get_numberOfDeliveries', 'weightInKg', 'payment', 'advancePayment', 'status', 'driverName', 'driverPhone', 'note')
    list_select_related = ('state', 'status')

    search_fields = ('route', 'driverName')
    list_filter = ('state', 'status')

    class Media:
        js = [
            'js/libs/jquery.maskedinput.min.js', 
            'js/admin/cargo.js'
        ]

    def get_row_classes(self, obj, index):
        if obj.status.code == 'CONTRATADA':
            return 'table-warning'
        if obj.status.code == 'CARREGANDO':
            return 'table-success'
        return ''

    @admin.display(ordering="numberOfDeliveries", description=_("Deliveries"))
    def get_numberOfDeliveries(self, obj):
        return obj.numberOfDeliveries

    @admin.display(ordering="state", description=_("State"))
    def get_state(self, obj):
        return obj.state.abbreviation
        

admin.site.register(User, CustomUserAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(CargoStatus)