FROM python:3.12-slim-bookworm

RUN useradd wagtail

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies.
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt gunicorn

WORKDIR /app

RUN chown wagtail:wagtail /app

COPY --chown=wagtail:wagtail . .

USER wagtail

# Collect static files (uses dummy secret key if not set).
RUN DJANGO_SETTINGS_MODULE=artoftheharbor.settings.dev python manage.py collectstatic --noinput --clear

CMD set -xe; python manage.py migrate --noinput; gunicorn artoftheharbor.wsgi:application
