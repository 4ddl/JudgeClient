broker_url: str = "redis://127.0.0.1/0"
result_backend: str = "redis://127.0.0.1/1"
enable_utc: bool = True
timezone: str = "Asia/Shanghai"
CELERY_TASK_SOFT_TIME_LIMIT = CELERY_TASK_TIME_LIMIT = 10 * 60
