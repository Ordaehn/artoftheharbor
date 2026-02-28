# Art of the Harbor

Portfolio website for Luis Islas — tattoo artist and fine artist from Carson, Los Angeles, CA.

## Architecture

Standard Django website with Wagtail used **only for the blog**. All other pages (home, about, gallery, contact) are plain Django models, views, and templates. Luis manages blog posts via Wagtail admin at `/admin/` and everything else via Django admin at `/django-admin/`.

## Tech Stack

- Python 3.12, Django 6.0, Wagtail 7.3 (blog only)
- HTMX for smooth page transitions
- PostgreSQL (production), SQLite (dev)
- WhiteNoise for static files, Gunicorn for WSGI
- Docker + Docker Compose for deployment

## Project Structure

```
artoftheharbor/          # Django project package
  settings/              # base.py, dev.py, production.py
  templates/             # base.html, 404.html, 500.html
  static/css/            # artoftheharbor.css (global styles)
  static/js/             # artoftheharbor.js (nav toggle + HTMX)
home/                    # HomePageContent, FeaturedWork — plain Django
about/                   # AboutPageContent — plain Django
gallery/                 # ArtworkImage, TattooImage, GalleryCategory — plain Django
contact/                 # ContactPageContent, ContactSubmission, ContactForm — plain Django
blog/                    # BlogIndexPage, BlogPage, BlogCategory — Wagtail
```

## URL Routing

```
/                    → home:home (Django view)
/about/              → about:about (Django view)
/gallery/artwork/    → gallery:artwork (Django view)
/gallery/tattoo/     → gallery:tattoo (Django view)
/contact/            → contact:contact (Django view)
/blog/               → Wagtail catch-all (BlogIndexPage)
/blog/<slug>/        → Wagtail catch-all (BlogPage)
/admin/              → Wagtail admin (blog management)
/django-admin/       → Django admin (all other content)
```

## Commands

```bash
# Dev server
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

# Set up Wagtail blog page tree (run once after fresh migrate)
python manage.py setup_blog

# Static files
python manage.py collectstatic --noinput

# System check
python manage.py check
```

## Docker

```bash
# Copy and configure environment
cp .env.example .env

# Build and start
docker compose up --build

# Create superuser
docker compose exec web python manage.py createsuperuser

# Set up blog page tree
docker compose exec web python manage.py setup_blog

# Site available at http://localhost:8000
```

## Settings

- Dev: `artoftheharbor.settings.dev` (default in manage.py, SQLite)
- Production: `artoftheharbor.settings.production` (requires DJANGO_SECRET_KEY, DATABASE_URL)

## Design

- Color scheme: black/white primary, navy (#1a2744) and light blue (#6fa8dc) accents
- Full-bleed background images with HTMX page transitions
- Nav: About | Artwork | Tattoos | Blog | Contact Me (static HTML, `{% url %}` tags)

## Content Management

- **Blog**: Managed via Wagtail admin (`/admin/`) — create/edit BlogPages
- **Everything else**: Managed via Django admin (`/django-admin/`) — singleton content models (HomePageContent, AboutPageContent, ContactPageContent) + gallery images (ArtworkImage, TattooImage)
