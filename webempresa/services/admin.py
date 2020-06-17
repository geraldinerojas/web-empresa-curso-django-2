from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', )
    list_display_links = ('title', )
    search_fields = ('title', )
    list_per_page = 10

    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)