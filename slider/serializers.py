from rest_framework import serializers

from slider.models import Slider


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title', 'image', 'description', 'order', 'created_at', 'updated_at',)
