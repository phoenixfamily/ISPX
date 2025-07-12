from rest_framework import serializers
from .models import Slider, CEO, CooperationRequest


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class CeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CEO
        fields = '__all__'


class CooperationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CooperationRequest
        fields = '__all__'
