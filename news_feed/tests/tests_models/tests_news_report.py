"""
Tests for app news_feed
"""

from textwrap import dedent

from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from news_feed.models import NewsReport

DEFAULT_DICT_NEWS = {
    'name': 'Test. Test2',
    'preview': 'test',
    'text': dedent('''\
        Here's a small example of an article.
        This is multi-line text.
        It respects left padding.
    ''').strip()
}
DEFAULT_ARRAY_PARAGRAPH_TEXT = [
    'Here\'s a small example of an article.',
    'This is multi-line text.',
    'It respects left padding.'
]
DEFAULT_SLUG = 'test-test2'


class NewsReportTestCase(TestCase):
    """Test for model NewsReport"""

    def setUp(self) -> None:
        self.news = NewsReport(**DEFAULT_DICT_NEWS)
        self.news.save()

    def test_true_raise_exception_when_creating_same_news(self) -> None:
        with self.assertRaises(IntegrityError):
            NewsReport(**DEFAULT_DICT_NEWS).save()

    def test_not_raise_exception_with_update_news_in_admin(self):
        news = NewsReport.objects.get(slug=DEFAULT_SLUG)

        assert self.news.id == news.id
        news.clean()  # no exception should be thrown when checking the object

    def test_true_raise_exception_with_create_news_in_admin(self):
        news = NewsReport(**DEFAULT_DICT_NEWS)

        with self.assertRaises(ValidationError):
            news.clean()

    def test_true_generate_slug(self):
        assert DEFAULT_SLUG == self.news.slug

    def test_get_array_paragraph_text(self) -> None:
        assert DEFAULT_ARRAY_PARAGRAPH_TEXT == self.news.array_paragraph_text()
