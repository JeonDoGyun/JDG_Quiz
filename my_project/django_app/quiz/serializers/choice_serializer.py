from rest_framework import serializers


class ChoiceCreateSerializer(serializers.Serializer):
    text = serializers.CharField()
    is_answer = serializers.BooleanField()


class ChoiceUpdateSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    text = serializers.CharField()
    is_answer = serializers.BooleanField()
