
from django.apps import AppConfig


class OurprofileConfig(AppConfig):
    name = 'OurProfile'
    def ready(self):
        import OurProfile.signals