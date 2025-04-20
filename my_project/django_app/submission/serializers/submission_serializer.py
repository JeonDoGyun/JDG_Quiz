from rest_framework import serializers

from ..serializers.submission_answer_serializer import SubmissionAnswerInputSerializer


class SubmissionSubmitSerializer(serializers.Serializer):
    answers = SubmissionAnswerInputSerializer(many=True)

    def validate_answers(self, value):
        if not value:
            raise serializers.ValidationError("답안은 최소 하나 이상 제출되어야 합니다.")
        return value
