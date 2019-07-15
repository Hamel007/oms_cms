from django.db import models
from oms_gallery.models import Gallery

from oms_cms.backend.languages.models import AbstractLang


class InfoBlock(AbstractLang):
    """Модель инфо блока"""
    SECTIONS = (
        ("display", "главный экран"),
        ("header", "верх"),
        ("left", "лево"),
        ("right", "право"),
        ("footer", "низ"),
        ("centre", "центр"),
    )
    title = models.CharField("Заголовок", max_length=100)
    sub_title = models.CharField("Под заголовок", max_length=100, blank=True, null=True)
    desc = models.TextField("Описание", max_length=1000, blank=True)
    slider = models.ForeignKey(
        Gallery,
        verbose_name="Слайдер",
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    section = models.CharField(
        "Расположение",
        max_length=10,
        choices=SECTIONS,
        unique=True
    )

    class Meta:
        verbose_name = "Инфо блок"
        verbose_name_plural = "Инфо блок"

    def __str__(self):
        return self.title
