from django.db import models


class HomePageContent(models.Model):
    hero_image = models.ImageField(upload_to="home/", blank=True)
    hero_title = models.CharField(max_length=255, default="Art of the Harbor")
    hero_subtitle = models.CharField(max_length=255, blank=True)
    hero_cta_text = models.CharField("CTA button text", max_length=50, default="View My Work")
    hero_cta_link = models.URLField(blank=True, help_text="URL for the CTA button")
    intro = models.TextField(blank=True)
    philosophy_statement = models.TextField(blank=True)

    class Meta:
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Content"

    def __str__(self):
        return "Home Page"


class FeaturedWork(models.Model):
    image = models.ImageField(upload_to="home/featured/")
    caption = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "Featured Work"
        verbose_name_plural = "Featured Works"

    def __str__(self):
        return self.caption or f"Featured Work #{self.pk}"
