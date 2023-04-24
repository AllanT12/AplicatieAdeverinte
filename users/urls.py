from django.urls import path, include
from .views import *
from rest_framework.authtoken import views


urlpatterns = [
    path('register/', UserAPIView.as_view()),
    path('delete/', UserAPIView.as_view()),
    path('login/', views.obtain_auth_token),
    path('update/', UserAPIView.as_view()),
]