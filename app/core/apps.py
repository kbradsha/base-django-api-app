from django.apps import AppConfig


class CoreConfig(AppConfig):
    """ Django Core configuration class """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
