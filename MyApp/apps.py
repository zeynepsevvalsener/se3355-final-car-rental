from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Optional: ensures correct ID field type
    name = 'MyApp'  # Ensure this matches your app’s folder name

    def ready(self):
        """This method is called when the app is fully loaded."""
        # Import models or signals here, not at the top level
        from django.contrib.auth.models import User  # Safe to import inside ready()
        import MyApp.signals  # If using signals, import them here
