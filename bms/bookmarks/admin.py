from django.contrib import admin

from .models import Page, Bookmark


@admin.register(Page)
class PageModelAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'title',
        'created_date',
        )


@admin.register(Bookmark)
class BookmarkModelAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'page',
        'tag_list',
        'created_date',
        )
    fieldsets = (
        (None, {
            'fields': (
                'user',
                'page',
                'tags',
                ),
            }),
        ('Advanced options', {
            'classes': ('collapse', ),
            'fields': (
                'name',
                'comment',
                'star',
                'archived',
                ),
            }),
        )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())
    tag_list.short_description = Bookmark.tags.through.tag_model()._meta.verbose_name
