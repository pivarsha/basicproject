from django.urls import path
from .views import *

app_name="first"

urlpatterns = [
    path('apps_1/',HomePage.as_view(),name='apps_1'),
]
