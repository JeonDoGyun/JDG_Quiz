from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..repositories.question_repository import QuestionRepository
from ..repositories.choice_repository import ChoiceRepository
from ..serializers.question_serializer import QuestionCreateSerializer
from ..models.question import Question
from ..models.choice import Choice
from ..services.question_service import QuestionService
from ..services.choice_service import ChoiceService
from ..docs.question_docs import question_create_docs


from user.permissions.roles import IsAdmin


# choice가 question 안에 포함되는 내용이기 때문에 같이 작성
class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    question_repository = QuestionRepository()
    choice_repository = ChoiceRepository()
    question_service = QuestionService(question_repository)
    choice_service = ChoiceService(choice_repository)

    @question_create_docs
    def post(self, request):
        serializer = QuestionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 문제 생성
        question = Question(
            quiz_id=serializer.validated_data["quiz_id"],
            content=serializer.validated_data["description"]
        )
        saved_question = self.question_service.create_question(question)

        # 보기 생성
        choices_data = serializer.validated_data["choices"]
        choices = [
            Choice(
                question_id=saved_question.id,
                content=choice["text"],
                is_answer=choice["is_answer"]
            )
            for choice in choices_data
        ]
        self.choice_service.add_choices_to_question(choices)

        return Response(
            {
                "message": "문제와 보기 등록 완료",
                "question_id": str(saved_question.id)
            },
            status=status.HTTP_201_CREATED
        )
