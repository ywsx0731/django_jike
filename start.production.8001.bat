# for async web server:
workon django_recruitment
export DJANGO_SETTINGS_MODULE=settings.online
uvicorn recruitment.asgi:application --port 8001 --workers 2