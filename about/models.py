from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.blocks import CharBlock, RichTextBlock, TextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images import get_image_model_string
from wagtail.models import Page


class AboutPage(Page):
    portrait_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    subtitle = models.CharField(max_length=255, blank=True)
    body = StreamField(
        [
            ("heading", CharBlock(form_classname="title")),
            ("paragraph", RichTextBlock()),
            ("quote", TextBlock(icon="openquote")),
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("portrait_image"),
        FieldPanel("subtitle"),
        FieldPanel("body"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    class Meta:
        verbose_name = "About Page"
