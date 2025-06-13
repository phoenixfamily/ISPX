from rest_framework import serializers
from .models import Slider, CEO


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class CeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CEO
        fields = '__all__'
