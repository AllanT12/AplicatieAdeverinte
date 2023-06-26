from rest_framework import serializers

from setari.models import Setari


class SetariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setari
        fields = '__all__'