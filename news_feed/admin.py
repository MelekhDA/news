"""
Register models from app of news_feed
"""

from django.contrib import admin
from .models import NewsReport


class NewsReportAdmin(admin.ModelAdmin):
    exclude = ("slug ",)
    readonly_fields = ('slug', 'date_created')


admin.site.register(NewsReport, NewsReportAdmin)
