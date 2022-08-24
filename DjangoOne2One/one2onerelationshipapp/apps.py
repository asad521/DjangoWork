from django.apps import AppConfig


class One2OnerelationshipappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'one2onerelationshipapp'
    
    def read(self):
        import one2onerelationshipapp.signal