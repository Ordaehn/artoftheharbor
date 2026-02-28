from django.core.management.base import BaseCommand

from wagtail.models import Page, Site

from blog.models import BlogIndexPage


class Command(BaseCommand):
    help = "Create BlogIndexPage under Wagtail root and configure the default Site"

    def handle(self, *args, **options):
        root = Page.objects.filter(depth=1).first()
        if not root:
            self.stderr.write("Wagtail root page not found.")
            return

        # Delete the default "Welcome to Wagtail" page if it exists
        for child in Page.objects.filter(depth=2):
            if not isinstance(child.specific, BlogIndexPage):
                child.delete()
                self.stdout.write(f"Deleted page: {child.title}")

        # Fix root numchild after deletions
        root.numchild = Page.objects.filter(depth=2).count()
        root.save(update_fields=["numchild"])

        # Create BlogIndexPage if it doesn't exist
        if not BlogIndexPage.objects.exists():
            blog_index = BlogIndexPage(
                title="Blog",
                slug="",
                show_in_menus=True,
            )
            root.add_child(instance=blog_index)
            blog_index.save_revision().publish()
            self.stdout.write(self.style.SUCCESS("Created BlogIndexPage"))
        else:
            blog_index = BlogIndexPage.objects.first()
            self.stdout.write("BlogIndexPage already exists")

        # Configure default Site to point at blog_index (Wagtail requires a root page)
        site, created = Site.objects.get_or_create(
            is_default_site=True,
            defaults={
                "hostname": "localhost",
                "port": 8001,
                "site_name": "Art of the Harbor",
                "root_page": blog_index,
            },
        )
        if not created:
            site.root_page = blog_index
            site.site_name = "Art of the Harbor"
            site.save()
            self.stdout.write("Updated default Site")
        else:
            self.stdout.write(self.style.SUCCESS("Created default Site"))
