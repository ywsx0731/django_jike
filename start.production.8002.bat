# for async web server:
export DJANGO_SETTINGS_MODULE=settings.online
uvicorn recruitment.asgi:application --port 8002 --workers 2