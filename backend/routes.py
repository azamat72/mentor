from django.urls import path
from . views import *


urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('news', news, name="news"),
    path('events', events, name="events"),
    path('agents', agents, name="agents"),
    path('contact', contact, name="contact"),
    
]
