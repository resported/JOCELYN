from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email')
    list_display = ('username', 'email')


admin.site.register(User, UserAdmin)