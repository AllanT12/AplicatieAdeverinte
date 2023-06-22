from rest_framework import serializers

from specializari.models import Specializari


class SpecializariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specializari
        fields = ['id', 'nume', 'acronim', 'is_master']