from django.contrib import admin
from django.urls import path, include

from adeverinte.views import AdeverintaAPIView

urlpatterns = [
    path('crate/', AdeverintaAPIView.as_view()),
    path('delete/<int:pk>', AdeverintaAPIView.as_view()),
    path('update/<int:pk>', AdeverintaAPIView.as_view()),
    path('downloadPDF/<int:pk>', AdeverintaAPIView.as_view()),
    path('get/<int:pk>', AdeverintaAPIView.as_view()),
]