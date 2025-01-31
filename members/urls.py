from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL of the 'members' app, linked to 'home' view
]