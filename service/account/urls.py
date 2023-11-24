from django.urls import path
from .views import registration_view

app_name = 'account'

urlpatterns = [
    path('registration/', registration_view, name='registration'),
]
