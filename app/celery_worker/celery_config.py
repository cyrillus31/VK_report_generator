from celery import Celery

from config import settings

celery_app = Celery("tasks", broker=f"pyamqp://{settings.rabbit_name}:{settings.rabbit_password}@{settings.rabbit_host}:{settings.rabbit_port}")
