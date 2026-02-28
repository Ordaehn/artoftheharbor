from django.contrib import admin

from .models import ContactPageContent, ContactSubmission


@admin.register(ContactPageContent)
class ContactPageContentAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email_to"]

    def has_add_permission(self, request):
        return not ContactPageContent.objects.exists()


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "submitted_at"]
    readonly_fields = ["name", "email", "message", "submitted_at"]
    ordering = ["-submitted_at"]

    def has_add_permission(self, request):
        return False
