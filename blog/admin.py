from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'parent', 'is_active']
    list_filter = ['parent', 'is_active']
    list_editable = ['url', 'parent', 'is_active']
    list_display_links = ['title']
    search_fields = ['title', 'url']
    ordering = ['parent', 'id']

admin.site.register(MenuItem, MenuItemAdmin)