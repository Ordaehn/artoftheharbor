from django.shortcuts import render

from .models import AboutPageContent


def about(request):
    content = AboutPageContent.objects.first()
    return render(request, "about/about_page.html", {
        "content": content,
    })
