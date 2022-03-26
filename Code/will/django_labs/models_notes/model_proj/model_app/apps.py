from django.apps import AppConfig


class ModelAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_app'
