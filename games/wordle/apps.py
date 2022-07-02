from django.apps import AppConfig


class WordleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wordle'

    def ready(self):
        import wordle.signals