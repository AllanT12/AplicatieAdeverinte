from rest_framework import serializers

from specializari.models import Specializari


class SpecializariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specializari
        fields = '__all__'