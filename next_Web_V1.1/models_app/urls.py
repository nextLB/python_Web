from django.urls import path
from . import views

app_name = 'models_app'

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('self-supervised/', views.self_supervised, name='self_supervised'),
    path('supervised/', views.supervised, name='supervised'),
    path('select-model/<str:model_type>/<str:model_name>/', views.select_model, name='select_model'),
]
