from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Orderable, Page
from wagtail.snippets.models import register_snippet


@register_snippet
class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)

    panels = [
        FieldPanel("name"),
    ]

    class Meta:
        verbose_name_plural = "Gallery Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ArtworkGalleryPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        InlinePanel("artwork_images", label="Artwork"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    class Meta:
        verbose_name = "Artwork Gallery"


class ArtworkGalleryImage(Orderable):
    page = ParentalKey(
        ArtworkGalleryPage, on_delete=models.CASCADE, related_name="artwork_images"
    )
    image = models.ForeignKey(
        get_image_model_string(),
        on_delete=models.CASCADE,
        related_name="+",
    )
    caption = models.CharField(max_length=255, blank=True)
    medium = models.CharField(max_length=100, blank=True, help_text="e.g. Oil on canvas")
    year = models.CharField(max_length=10, blank=True)
    category = models.ForeignKey(
        GalleryCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
        FieldPanel("medium"),
        FieldPanel("year"),
        FieldPanel("category"),
    ]


class TattooGalleryPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        InlinePanel("tattoo_images", label="Tattoos"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    class Meta:
        verbose_name = "Tattoo Gallery"


class TattooGalleryImage(Orderable):
    page = ParentalKey(
        TattooGalleryPage, on_delete=models.CASCADE, related_name="tattoo_images"
    )
    image = models.ForeignKey(
        get_image_model_string(),
        on_delete=models.CASCADE,
        related_name="+",
    )
    caption = models.CharField(max_length=255, blank=True)
    style = models.CharField(max_length=100, blank=True, help_text="e.g. Blackwork, Realism")
    body_placement = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(
        GalleryCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
        FieldPanel("style"),
        FieldPanel("body_placement"),
        FieldPanel("category"),
    ]
