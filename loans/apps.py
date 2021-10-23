from django.apps import AppConfig


class LoansAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loans'  
    def ready(self):
     # import your signal file in here if the app is ready
        from . import models