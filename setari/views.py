from django.http import JsonResponse
from django.shortcuts import render
from injector import inject
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from setari.serializer import SetariSerializer
from setari.services import SetariService


# Create your views here.
class SetariAPIView(APIView):
    permission_classes = [AllowAny]

    @inject
    def setup(self, request, my_service: SetariService, **kwargs):
        self.service = my_service
        self.request = request
        self.kwargs = kwargs

    def get(self, request):
        user = self.service.get_all()
        data = SetariSerializer(user, many=True)
        return JsonResponse(status=200, data=data.data, safe=False)

    def post(self, request):
        user = SetariSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(user.errors, status=300)
