"""
Views from app of news_feed
"""

from django.views import generic

from .models import NewsReport

DEFAULT_TEMPLATE_PACKAGE = 'news_feed'
DEFAULT_PAGINATE = 5


class MainPageNewsView(generic.TemplateView):
    """Main page (homepage) template news"""

    template_name = f"{DEFAULT_TEMPLATE_PACKAGE}/main_page_news.html"


class ListNewsRecordView(generic.ListView):
    """List news (with pagination)"""

    model = NewsReport
    template_name = f'{DEFAULT_TEMPLATE_PACKAGE}/list_news.html'
    context_object_name = 'news_reports'
    paginate_by = DEFAULT_PAGINATE
    queryset = NewsReport.objects.filter(is_active=True).order_by('-date_created')


class NewsDetailView(generic.DetailView):
    """News details"""

    model = NewsReport
    context_object_name = 'news'
    template_name = f'{DEFAULT_TEMPLATE_PACKAGE}/news_detail.html'
