from rest_framework import serializers

from adeverinte.models import Adeverinta


class AdeverinteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adeverinta
        fields = '__all__'