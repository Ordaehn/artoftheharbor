from django.shortcuts import render

from .models import ArtworkImage, TattooImage


def artwork(request):
    images = ArtworkImage.objects.select_related("category").all()
    return render(request, "gallery/artwork_gallery_page.html", {
        "images": images,
    })


def tattoo(request):
    images = TattooImage.objects.select_related("category").all()
    return render(request, "gallery/tattoo_gallery_page.html", {
        "images": images,
    })
