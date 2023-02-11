from django.urls import path
from .views import *

app_name="second"

urlpatterns = [
    path('apps_2/',HomePage.as_view(),name='apps_2'),
]
