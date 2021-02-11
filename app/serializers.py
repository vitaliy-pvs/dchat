from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.Serializer):
    timestamp = serializers.IntegerField()
    username = serializers.CharField(max_length=50)
    body = serializers.CharField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
