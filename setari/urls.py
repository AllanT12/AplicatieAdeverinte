from django.urls import path, include

from setari.views import SetariAPIView

urlpatterns = [
    path('crate/', SetariAPIView.as_view()),
]