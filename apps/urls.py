from django.urls import path
from .views import *

app_name="home"

urlpatterns = [
    path('',HomePage.as_view(),name='index'),
]
