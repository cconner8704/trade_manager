from celery import Celery
# Celery configuration
CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
CELERY_RESULT_BACKEND = 'rpc://'
# Initialize Celery
celery = Celery('workerB', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
@celery.task()
def sub_nums(a, b):
   return a - b