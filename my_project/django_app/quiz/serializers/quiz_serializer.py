from rest_framework import serializers
from ..models.question import Quiz


class QuizCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            "title", "description", "num_questions", "page_size",
            "shuffle_option", "shuffle_question", "created_by"
        ]


class QuizUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            "title", "description", "num_questions", "page_size",
            "shuffle_option", "shuffle_question"
        ]
