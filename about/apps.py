from django.apps import AppConfig


class AboutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'

    def ready(self):
            import about.translation  # <-- MUHIM
