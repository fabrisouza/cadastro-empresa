from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Client, Company, Manager


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_admin',
                'groups',
                'user_permissions',
            )
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'cpf', 'email', 'company_id']
    exclude = ['cnpj']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['cnpj', 'name', 'address', 'city', 'email']
    exclude = ['first_name', 'last_name', 'cpf', 'company_id']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['company_id']
    exclude = ['cnpj', 'name', 'address', 'city', 'email', 'first_name', 'last_name', 'cpf',]
    

admin.site.register(User, UserAdmin)