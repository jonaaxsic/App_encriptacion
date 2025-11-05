from django.urls import path
from . import views

app_name = 'encryptor'

urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.process_crypto, name='process'),
]