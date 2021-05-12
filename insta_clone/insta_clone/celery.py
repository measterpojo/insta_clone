import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram_clone.settings')

# IMPORTANT check the name of your project and replace it here 'yourproject'
app = Celery('insta_clone')

app.config_from_object('django.conf:settings', namespace='INSTA')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')