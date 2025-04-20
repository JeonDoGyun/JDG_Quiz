from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..serializers.submission_serializer import SubmissionSubmitSerializer
from ..services.submission_service import SubmissionService
from ..repositories.submission_repository import SubmissionRepository
from ..docs.submission_docs import answer_submit_docs


class SubmissionSubmitView(APIView):
    permission_classes = [IsAuthenticated]
    submission_repository = SubmissionRepository()
    submission_service = SubmissionService()

    @answer_submit_docs
    def post(self, request, submission_id):
        submission = self.submission_repository.get_submission_by_id(
            submission_id)

        if submission.submitted_at:
            return Response(
                {"message": "이미 제출된 응시 내역이 있습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SubmissionSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answers_data = serializer.validated_data["answers"]

        updated_submission = self.submission_service.submit_answers(
            submission, answers_data)
        total_count = len(answers_data)

        return Response(
            {
                "score": updated_submission.score,
                "message": f"{total_count}개의 문항 중 {updated_submission.score}개 맞추셨습니다."
            },
            status=status.HTTP_200_OK
        )
