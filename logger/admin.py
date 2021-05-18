from django.contrib import admin
from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('method', 'path', 'execution_time_sec')


admin.site.site_header = 'Hello Administration'
