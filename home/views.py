from django.shortcuts import render

from .models import FeaturedWork, HomePageContent


def home(request):
    content = HomePageContent.objects.first()
    featured_works = FeaturedWork.objects.all()
    return render(request, "home/home_page.html", {
        "content": content,
        "featured_works": featured_works,
    })
