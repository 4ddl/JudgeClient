import os
from celery import Celery
from judge_client.service import default_config

app = Celery(include=['judge_client.service.tasks'])

if os.environ.get('CELERY_CONFIG'):
    app.config_from_envvar('CELERY_CONFIG')
else:
    print('Environ "CELERY_CONFIG" not found, use default celery config')
    app.config_from_object(default_config)
