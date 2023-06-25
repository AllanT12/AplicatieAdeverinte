from rest_framework import serializers

from adeverinte.models import Adeverinta
from users.serializer import UserSerializer, UserSerializerOut


class AdeverinteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adeverinta
        fields = '__all__'


class AdeverinteSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Adeverinta
        fields = '__all__'
    subsemnatul = UserSerializerOut(many=False)
    stare = serializers.CharField(source='get_stare_display')

