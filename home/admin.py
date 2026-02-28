from django.contrib import admin

from .models import FeaturedWork, HomePageContent


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ["__str__"]

    def has_add_permission(self, request):
        return not HomePageContent.objects.exists()


@admin.register(FeaturedWork)
class FeaturedWorkAdmin(admin.ModelAdmin):
    list_display = ["caption", "sort_order"]
    list_editable = ["sort_order"]
    ordering = ["sort_order"]
