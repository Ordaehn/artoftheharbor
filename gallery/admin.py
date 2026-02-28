from django.contrib import admin

from .models import ArtworkImage, GalleryCategory, TattooImage


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(ArtworkImage)
class ArtworkImageAdmin(admin.ModelAdmin):
    list_display = ["caption", "medium", "year", "category", "sort_order"]
    list_editable = ["sort_order"]
    list_filter = ["category"]
    ordering = ["sort_order"]


@admin.register(TattooImage)
class TattooImageAdmin(admin.ModelAdmin):
    list_display = ["caption", "style", "body_placement", "category", "sort_order"]
    list_editable = ["sort_order"]
    list_filter = ["category"]
    ordering = ["sort_order"]
