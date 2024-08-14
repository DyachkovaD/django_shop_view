import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_view_project.settings')
app = Celery('shop_view_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()