from django.apps import AppConfig
from server.settings import mongo_connect  # Adjust import path if needed


class MlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ml'

    def ready(self):
        mongo_connect()  # Connect to MongoDB when app is ready
