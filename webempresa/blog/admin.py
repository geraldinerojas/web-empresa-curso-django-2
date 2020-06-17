from django.contrib import admin
from .models import Post, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated', )
    list_display_links = ('name', )
    list_filter = ('name', )
    list_per_page = 10
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'post_categories', )
    list_display_links = ('title', )
    ordering = ('author', 'published', )
    search_fields = ('title', 'content', 'author__username',)
    list_filter = ('categories', 'author__username', )
    date_hierarchy = 'published'
    list_per_page = 10
    readonly_fields = ('created', 'updated')

    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])

    post_categories.short_description = 'Categorías'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)