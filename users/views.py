from django.http import JsonResponse
from django.shortcuts import render
from injector import inject
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializer import UserSerializer, UserSerializerOut
from users.services import UserService


# Create your views here.
class UserAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (TokenAuthentication,)

    @inject
    def setup(self, request, my_service: UserService, **kwargs):
        self.service = my_service
        self.request = request
        self.kwargs = kwargs

    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            self.service.encrypt(user=user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(user.errors, status=300)

    def patch(self, request):
        token = request.auth
        user = self.service.get(token.user_id)
        data = UserSerializer(user, many=False)
        if data.is_valid():
            data.save()
            return JsonResponse(status=202, data=data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        token = request.auth
        self.service.delete(token.user_id)
        return Response(status=status.HTTP_202_ACCEPTED)

    def get(self, request):
        token = request.auth
        user = self.service.get(token.user_id)
        data = UserSerializer(user, many=False)
        return JsonResponse(status=200, data=data.data, safe=False)

    def put(self, request):
        user = self.service.get_all()
        data = UserSerializerOut(user, many=True)
        return JsonResponse(status=202, data=data.data, safe=False)
