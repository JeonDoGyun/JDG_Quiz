from rest_framework import serializers


class SubmissionAnswerInputSerializer(serializers.Serializer):
    question_id = serializers.UUIDField()
    selected_choice_id = serializers.UUIDField()
