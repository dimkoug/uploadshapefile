import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uploadshape.settings')

app = Celery('uploadshape')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379'
app.conf.result_backend = 'redis://localhost:6379'
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
