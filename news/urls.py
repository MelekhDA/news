"""
App of news url configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('news-feed/', include('news_feed.urls')),
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('news-feed/main-page-news/'))
]
