from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'
    # Import signals in our app.
    def ready(self):
        import profiles.signals