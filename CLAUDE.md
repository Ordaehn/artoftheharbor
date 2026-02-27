# Art of the Harbor

Portfolio website for Luis Islas — tattoo artist and fine artist from Carson, Los Angeles, CA.

## Tech Stack

- Python 3.12, Django 6.0, Wagtail 7.3
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
home/                    # HomePage model + template
gallery/                 # ArtworkGalleryPage, TattooGalleryPage, GalleryCategory snippet
blog/                    # BlogIndexPage, BlogPage, BlogCategory snippet
about/                   # AboutPage with StreamField
contact/                 # ContactPage (AbstractEmailForm)
search/                  # Wagtail search view
```

## Commands

```bash
# Dev server
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

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

# Site available at http://localhost:8000
```

## Settings

- Dev: `artoftheharbor.settings.dev` (default in manage.py, SQLite)
- Production: `artoftheharbor.settings.production` (requires DJANGO_SECRET_KEY, DATABASE_URL)

## Design

- Color scheme: black/white primary, navy (#1a2744) and light blue (#6fa8dc) accents
- Full-bleed background images with HTMX page transitions
- Nav: Home | About | My Work | Blog | Contact Me
- Pages shown in nav must have "Show in menus" checked in Wagtail admin

## Page Hierarchy

```
Root (Home)
├── About
├── Artwork Gallery (My Work sub-tab)
├── Tattoo Gallery (My Work sub-tab)
├── Blog Index
│   └── Blog Post (children)
└── Contact Me
```
