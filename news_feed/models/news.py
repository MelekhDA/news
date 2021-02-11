"""
Model of news
"""

from django.db import models
from slugify import slugify
from django.core.exceptions import ValidationError
from annoying.functions import get_object_or_None

MAX_LENGTH_NAME_NEWS = 250
MAX_LENGTH_CLEAN_URL = 2048
MAX_LENGTH_PREVIEW = 500


class NewsReport(models.Model):
    """
    Class news

    Fields of new:
        name of new
        clean url (or friendly url)
        preview of new
        text of new,
        flag of activity
        data of creation
    """

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статья'

    name = models.CharField(
        verbose_name='Название статьи',
        max_length=MAX_LENGTH_NAME_NEWS,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='ЧПУ',
        unique=True,
        max_length=MAX_LENGTH_NAME_NEWS * 2,
        auto_created=True
    )
    preview = models.CharField(
        verbose_name='Превью',
        max_length=MAX_LENGTH_PREVIEW
    )
    text = models.TextField(
        verbose_name='Текст статьи'
    )
    is_active = models.BooleanField(
        verbose_name='Флаг активности',
        default=True
    )
    date_created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_created=True,
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        """Save method with slug"""

        self.slug = slugify(self.name, to_lower=True)
        super().save(*args, **kwargs)

    def clean(self):
        """
        Method should be used to provide custom model validation,
        and to modify attributes on your model if desired
        (see: https://docs.djangoproject.com/en/3.1/ref/models/instances/)

        :return: None
        """

        slug = slugify(self.name, to_lower=True)
        news_report = get_object_or_None(NewsReport, slug=slug)

        if news_report is not None and self.id != news_report.id:
            raise ValidationError(
                'ЧПУ уже существует. '
                'Возможно, вы вводите название новости, похожее на существующее.'
            )

    def array_paragraph_text(self) -> list:
        """
        Get a list of paragraphs of news text

        :return: list of paragraphs
        """

        return self.text.split('\n')

    def __str__(self) -> str:
        prefix_name = self.name[:30]
        if len(self.name) > 30:
            prefix_name += '...'

        return f'{self.id} | {prefix_name}'
