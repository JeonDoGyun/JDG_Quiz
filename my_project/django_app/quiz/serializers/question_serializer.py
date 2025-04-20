from rest_framework import serializers

from ..serializers.choice_serializer import ChoiceCreateSerializer


class QuestionCreateSerializer(serializers.Serializer):
    quiz_id = serializers.UUIDField()
    description = serializers.CharField()
    choices = ChoiceCreateSerializer(many=True)

    def validate_choices(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("선택지는 최소 3개 이상이어야 합니다.")
        if [choice['is_answer'] for choice in value].count(True) != 1:
            raise serializers.ValidationError("정답은 정확히 1개여야 합니다.")
        return value


class QuestionUpdateSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    description = serializers.CharField()
