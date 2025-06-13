from rest_framework import serializers
from .models import Services


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

    def create(self, validated_data):
        service = Services.objects.create(**validated_data)
        return service

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.save()
        return instance
