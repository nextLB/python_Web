from django.apps import AppConfig


class ModelsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models_app'
    verbose_name = '模型选择应用'
