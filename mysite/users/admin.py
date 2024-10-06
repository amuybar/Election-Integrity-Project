from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Define the admin configuration for the CustomUser model
class CustomUserAdmin(UserAdmin):
    # Define fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    
    # Add 'role' to the fieldsets and the add_fieldsets for the form view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'role')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'role', 'is_staff', 'is_active')}
        ),
    )
    
    # Fields to search within the admin interface
    search_fields = ('username', 'email', 'role')

    # Define filters available in the admin list view
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')

    # Field ordering in the list view
    ordering = ('username',)

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
