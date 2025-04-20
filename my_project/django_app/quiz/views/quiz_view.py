from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..repositories.quiz_repository import QuizRepository
from ..serializers.quiz_serializer import QuizCreateSerializer, QuizUpdateSerializer
from ..models.quiz import Quiz
from ..services.quiz_service import QuizService

from user.permissions.roles import IsAdmin


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    quiz_repository = QuizRepository()
    quiz_service = QuizService(quiz_repository=quiz_repository)

    def get_serializer_class(self):
        if self.action == "create":
            return QuizCreateSerializer
        if self.action in ["update", "partial_update"]:
            return QuizUpdateSerializer
        return QuizCreateSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        quiz = Quiz(**serializer.validated_data)
        created_quiz = self.quiz_service.create_quiz(quiz)

        return Response(QuizCreateSerializer(created_quiz).data, status=status.HTTP_201_CREATED)

    def update(self, request, quiz_id=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        updated_quiz = Quiz(id=quiz_id, **serializer.validated_data)
        result = self.quiz_service.update_quiz(updated_quiz)

        return Response(QuizUpdateSerializer(result).data, status=status.HTTP_200_OK)

    def destroy(self, request, quiz_id=None):
        self.quiz_service.delete_quiz(quiz_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
