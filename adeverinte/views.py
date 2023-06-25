import csv

from django.http import JsonResponse, FileResponse, HttpResponse
from django.shortcuts import render
from injector import inject
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from adeverinte.serializer import AdeverinteSerializer, AdeverinteSerializerOut
from adeverinte.services import AdeverintaService


# Create your views here.
class AdeverintaAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (TokenAuthentication,)

    @inject
    def setup(self, request, my_service: AdeverintaService, **kwargs):
        self.service = my_service
        self.request = request
        self.kwargs = kwargs

    def post(self, request):
        token = request.auth
        request.data.update(self.service.create(request.data, token.user_id))
        user = AdeverinteSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(user.errors, status=300)

    def patch(self, request, pk):
        adeverinta = self.service.get(pk)
        data = AdeverinteSerializer(adeverinta, many=False)
        if data.is_valid():
            data.save()
            return JsonResponse(status=202, data=data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        device = self.service.get(nr=pk)
        device.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def put(self, request, pk):
        token = request.auth
        buffer = self.service.createPDF(pk, token.user_id)
        return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

    def patch(self, request, pk):
        token = request.auth
        if request.data["accept"]:
            self.service.Accept(pk, token.user_id)
        else:
            self.service.Deny(pk, token.user_id)
        return Response(status=status.HTTP_202_ACCEPTED)

    def get(self, request, pk):
        if pk == 1:
            adeverinte = self.service.getOnlyAccepted()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'
            writer = csv.DictWriter(response, fieldnames=['Nume', 'Motiv', 'Nr', 'Data'])
            writer.writeheader()
            for i in adeverinte:
                writer.writerow({'Nume': i.subsemnatul.first_name, 'Motiv': i.motivatie,'Nr': i.nr, 'Data': i.data})
            return response
        adeverinte = self.service.get_all()
        data = AdeverinteSerializerOut(adeverinte, many=True)
        return JsonResponse(status=200, data=data.data, safe=False)
