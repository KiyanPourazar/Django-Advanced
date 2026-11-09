from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm
# from django import forms

from .models import User, Profile


# class CustomUserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('email',)

class CustomUserAdmin(UserAdmin):
    model = User
    # add_form = CustomUserCreationForm
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('email',)

    fieldsets = (
        ('Authentication', {
            'fields': ('email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_active', 'is_staff')
        }),
        ('Group Permissions', {
            'fields': ('groups', 'user_permissions')
        }),
        ('important date', {
            'fields': ('last_login',)
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_superuser',
                'is_active',
                'is_staff',
            ),
        }),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
