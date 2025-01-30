from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  
    name = 'MyApp'  

    def ready(self):
        """This method is called when the app is fully loaded."""

        from django.contrib.auth.models import User 
        import MyApp.signals  
