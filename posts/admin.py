from django.contrib import admin
from . import models
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'created_at', 'post_type', 'group', 'image_thumbnail')
    list_filter = ('post_type', 'group', 'created_at', 'user')
    search_fields = ('message', 'user__username', 'group__name')
    readonly_fields = ('message_html', 'updated_at', 'created_at', 'image_thumbnail_display')

    fieldsets = (
        (None, {
            'fields': ('user', 'group')
        }),
        ('Post Content', {
            'fields': ('post_type', 'message', 'message_html', 'image', 'image_thumbnail_display')
        }),
        ('Observation Details (Optional)', {
            'fields': ('observation_date', 'location_description', 'equipment_used'),
            'classes': ('collapse',) # Collapsible section for less frequently edited fields
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "No Image"
    image_thumbnail.short_description = 'Image'

    def image_thumbnail_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" height="auto" />', obj.image.url)
        return "No Image Provided"
    image_thumbnail_display.short_description = 'Current Image Preview'


admin.site.register(models.Post, PostAdmin)
