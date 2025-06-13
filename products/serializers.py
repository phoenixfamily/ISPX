from rest_framework import serializers
from .models import Product
from category.models import Category


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        product = Product.objects.create(**validated_data)
        product.categories.set(categories_data)
        return product

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.video_title = validated_data.get('video_title', instance.video_title)
        instance.video = validated_data.get('video', instance.video)
        instance.save()
        instance.categories.set(categories_data)
        return instance
