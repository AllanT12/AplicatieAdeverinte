from django.urls import path

from specializari.views import SpecializariAPIView

urlpatterns = [
    path('create/', SpecializariAPIView.as_view()),
    path('delete/<int:pk>', SpecializariAPIView.as_view()),
    path('update/<int:pk>', SpecializariAPIView.as_view()),
    path('get/', SpecializariAPIView.as_view()),

]