from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Orderable, Page


class HomePage(Page):
    hero_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_title = models.CharField(max_length=255, blank=True, default="Art of the Harbor")
    hero_subtitle = models.CharField(max_length=255, blank=True)
    hero_cta_text = models.CharField(
        "CTA button text", max_length=50, blank=True, default="View My Work"
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    intro = RichTextField(blank=True)
    philosophy_statement = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_image"),
                FieldPanel("hero_title"),
                FieldPanel("hero_subtitle"),
                FieldPanel("hero_cta_text"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero Section",
        ),
        FieldPanel("intro"),
        InlinePanel("featured_works", label="Featured Works"),
        FieldPanel("philosophy_statement"),
    ]

    class Meta:
        verbose_name = "Home Page"


class HomePageFeaturedWork(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="featured_works")
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    caption = models.CharField(max_length=255, blank=True)
    link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
        FieldPanel("link"),
    ]
