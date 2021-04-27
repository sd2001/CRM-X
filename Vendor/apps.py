from django.apps import AppConfig


class VendorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Vendor'
    
    def ready(self):
        import Vendor.signals
