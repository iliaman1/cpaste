from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=128, unique=True, verbose_name=_('Категория'))

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title


class Paste(BaseModel):
    title = models.CharField(max_length=128, unique=True, verbose_name=_('Название'))
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name=_('Категория'))
    text = models.TextField(blank=True, verbose_name=_('Текст пасты'))

    class Meta:
        verbose_name = _('Паста')
        verbose_name_plural = _('Пасты')
