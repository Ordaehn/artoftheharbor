from django.db import models


class AboutPageContent(models.Model):
    portrait_image = models.ImageField(upload_to="about/", blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    bio_heading = models.CharField(max_length=255, blank=True)
    bio_text = models.TextField(blank=True)
    quote = models.TextField(blank=True)

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"

    def __str__(self):
        return "About Page"
