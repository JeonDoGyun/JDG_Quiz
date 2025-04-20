from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.quiz_view import QuizViewSet
from .views.question_view import QuestionCreateView

router = DefaultRouter()
router.register('quizzes', QuizViewSet, basename='quiz')

urlpatterns = [
    path('', include(router.urls)),  # /quizzes/
    path('questions/', QuestionCreateView.as_view(), name='question-create'),
]
