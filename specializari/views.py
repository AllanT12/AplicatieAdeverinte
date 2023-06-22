from django.http import JsonResponse
from django.shortcuts import render
from injector import inject
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from specializari.serializer import SpecializariSerializer
from specializari.services import SpecializariService


# Create your views here.
class SpecializariAPIView(APIView):
    permission_classes = [AllowAny]

    @inject
    def setup(self, request, my_service: SpecializariService, **kwargs):
        self.service = my_service
        self.request = request
        self.kwargs = kwargs

    def post(self, request):
        user = SpecializariSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(user.errors, status=300)

    def patch(self, request, pk):
        adeverinta = self.service.get(pk)
        data = SpecializariSerializer(adeverinta, many=False)
        if data.is_valid():
            data.save()
            return JsonResponse(status=202, data=data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        device = self.service.get(nr=pk)
        device.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def get(self, request):
        specializari = self.service.get_all()
        data = SpecializariSerializer(specializari, many=True)
        return JsonResponse(status=200, data=data.data, safe=False)
