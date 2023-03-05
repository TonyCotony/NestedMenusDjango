from django.contrib import admin

from app.models import MenuItem, MenuItemCategory


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'path', 'parent', 'is_visible')
    list_display_links = ('pk', 'name')
    search_fields = ('name', 'parent')
    list_editable = ('is_visible', )
    list_filter = ('is_visible', 'parent')
    prepopulated_fields = {'path': ('name', )}


class MenuItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'verbose_name')
    list_display_links = ('pk', 'name')
    search_fields = ('name', )


admin.site.register(MenuItem)
admin.site.register(MenuItemCategory)
