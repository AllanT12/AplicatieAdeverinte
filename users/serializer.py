from rest_framework import serializers

from specializari.serializer import SpecializariSerializer
from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
    specializare = SpecializariSerializer(many=True)
