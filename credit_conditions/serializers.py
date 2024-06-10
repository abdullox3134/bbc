from rest_framework import serializers

from credit_conditions.models import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id', 'title', 'description', 'file', 'created_at', 'updated_at',)
