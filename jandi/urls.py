from django.contrib import admin
from django.urls import path, include

from jandi.views import JandiAPIView

urlpatterns = [
    path('api/jandi/', JandiAPIView.as_view()),
]
