from django.contrib import admin

from .models import AboutPageContent


@admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    list_display = ["__str__"]

    def has_add_permission(self, request):
        return not AboutPageContent.objects.exists()
