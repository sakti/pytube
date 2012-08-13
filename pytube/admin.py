from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_time', 'view_count']
    search_fields = ['name', 'desc']
    date_hierarchy = 'created_time'


admin.site.register(Video, VideoAdmin)
