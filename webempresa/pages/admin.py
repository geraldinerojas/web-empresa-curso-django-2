from django.contrib import admin
from .models import Page


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('order', 'title',)
    list_display_links = ('title',)
    list_per_page = 10
    readonly_fields = ('created', 'updated')


admin.site.register(Page, PageAdmin)
