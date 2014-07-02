BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_IMPORTS = ("canvas_kaboom.chord_chain", )
CELERY_RESULT_BACKEND = "redis://localhost/1"
