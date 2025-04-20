from math import ceil
from uuid import UUID

from ..schemas.choice_schema import ChoiceSchema
from ..schemas.question_schema import QuestionSchema
from ..schemas.quiz_schema import QuizDetailResponse, QuizListItemSchema, QuizListResponseSchema

from django.core.paginator import Paginator
from django_app.quiz.models.quiz import Quiz
from django_app.submission.models.submission import Submission
from django_app.user.permissions.roles import Role



class QuizReadService:
    def get_quiz_list(self, role: Role, user_id: str, page: int, size: int) -> QuizListResponseSchema:
        quizzes = Quiz.objects.all().order_by("-created_at")
        paginator = Paginator(quizzes, size)
        page_obj = paginator.get_page(page)

        quiz_items = []
        for quiz in page_obj:
            has_submitted = None
            if role == Role.USER:
                has_submitted = Submission.objects.filter(
                    user_id=user_id,
                    quiz=quiz,
                    submitted_at__isnull=False
                ).exists()

            quiz_items.append(QuizListItemSchema(
                quiz_id=quiz.id,
                title=quiz.title,
                description=quiz.description,
                created_by=quiz.created_by.user_name,
                has_submitted=has_submitted
            ))

        return QuizListResponseSchema(
            quizzes=quiz_items,
            total=paginator.count,
            page=page,
            size=size
        )

    def get_quiz_detail(self, quiz_id: UUID, page: int) -> QuizDetailResponse:
        quiz = Quiz.objects.get(quiz_id=quiz_id)
        all_questions = list(quiz.question_set.all().order_by("created_at"))

        total_pages = ceil(len(all_questions) / quiz.page_size)
        start = (page - 1) * quiz.page_size
        end = start + quiz.page_size
        page_questions = all_questions[start:end]

        question_schema_list = []
        for question in page_questions:
            choices = question.choice_set.all()
            choice_schemas = [
                ChoiceSchema(choice_id=choice.id, text=choice.text)
                for choice in choices
            ]
            question_schema_list.append(
                QuestionSchema(
                    question_id=question.question_id,
                    description=question.description,
                    choices=choice_schemas
                )
            )

        return QuizDetailResponse(
            quiz_id=quiz.quiz_id,
            title=quiz.title,
            description=quiz.description,
            page=page,
            total_pages=total_pages,
            questions=question_schema_list
        )
