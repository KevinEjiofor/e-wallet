from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user_'
    default_auto_field = 'django.db.models.AutoField'


class MyAppConfig(AppConfig):
    name = 'user_'

    def ready(self):
        import user_.signals
