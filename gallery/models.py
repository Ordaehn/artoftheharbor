from django.db import models


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Gallery Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ArtworkImage(models.Model):
    image = models.ImageField(upload_to="gallery/artwork/")
    caption = models.CharField(max_length=255, blank=True)
    medium = models.CharField(max_length=100, blank=True, help_text="e.g. Oil on canvas")
    year = models.CharField(max_length=10, blank=True)
    category = models.ForeignKey(
        GalleryCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "Artwork Image"

    def __str__(self):
        return self.caption or f"Artwork #{self.pk}"


class TattooImage(models.Model):
    image = models.ImageField(upload_to="gallery/tattoo/")
    caption = models.CharField(max_length=255, blank=True)
    style = models.CharField(max_length=100, blank=True, help_text="e.g. Blackwork, Realism")
    body_placement = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(
        GalleryCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "Tattoo Image"

    def __str__(self):
        return self.caption or f"Tattoo #{self.pk}"
