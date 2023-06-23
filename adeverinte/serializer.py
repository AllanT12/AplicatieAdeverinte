from rest_framework import serializers

from adeverinte.models import Adeverinta
from users.serializer import UserSerializer


class AdeverinteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adeverinta
        fields = '__all__'
    #subsemnatul = UserSerializer(many=False)
