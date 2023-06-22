from django.urls import path, include
from .views import *
from rest_framework.authtoken import views


urlpatterns = [
    path('register/', UserAPIView.as_view()),
    path('delete/<int:pk>', UserAPIView.as_view()),
    path('login/', views.obtain_auth_token),
    path('update/<int:pk>', UserAPIView.as_view()),
    path('getuser/', UserAPIView.as_view()),
]