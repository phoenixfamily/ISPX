from rest_framework import serializers

from seo.models import SEOPage, Keyword


class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ["id", "name_en", "name_fa"]   # فیلدهای واقعی DB که modeltranslation ساخته

class SEOPageSerializer(serializers.ModelSerializer):
    # اگر بخواهی فقط id کیوردها را بگیری/بفرستی:
    keyword_ids = serializers.PrimaryKeyRelatedField(
        source="keywords", many=True, queryset=Keyword.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = SEOPage
        fields = [
            "page_url",
            "title_en", "title_fa",
            "description_en", "description_fa",
            "keyword_ids",
        ]
