from django.db import models


class ContactPageContent(models.Model):
    intro = models.TextField(blank=True)
    thank_you_text = models.TextField(blank=True)
    email_to = models.EmailField(blank=True, help_text="Email address to receive contact form submissions")

    class Meta:
        verbose_name = "Contact Page Content"
        verbose_name_plural = "Contact Page Content"

    def __str__(self):
        return "Contact Page"


class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Contact Submission"

    def __str__(self):
        return f"{self.name} — {self.submitted_at:%Y-%m-%d %H:%M}"
