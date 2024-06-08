from rest_framework import serializers

from about.models import About


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'description', 'image', 'created_at', 'updated_at',)
