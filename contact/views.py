from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import ContactPageContent, ContactSubmission


def contact(request):
    content = ContactPageContent.objects.first()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactSubmission.objects.create(**form.cleaned_data)

            # Send email if configured
            if content and content.email_to:
                send_mail(
                    subject=f"Contact form: {form.cleaned_data['name']}",
                    message=form.cleaned_data["message"],
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[content.email_to],
                    fail_silently=True,
                )

            return render(request, "contact/contact_page_landing.html", {
                "content": content,
            })
    else:
        form = ContactForm()

    return render(request, "contact/contact_page.html", {
        "content": content,
        "form": form,
    })
