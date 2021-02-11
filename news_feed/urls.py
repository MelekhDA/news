"""
App of news_feed url configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('main-page-news/', views.MainPageNewsView.as_view()),
    path('news/', views.ListNewsRecordView.as_view()),
    path('news/<slug:slug>', views.NewsDetailView.as_view())
]
