from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StatusUpdate

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Profile Info', {
            'fields': ('is_student', 'is_teacher', 'photo', 'bio'),
        }),
    )

# using our new CustomUserAdmin instead of the default one
admin.site.register(User, CustomUserAdmin)
admin.site.register(StatusUpdate)