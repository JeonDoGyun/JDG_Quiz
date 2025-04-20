from submission.models.submission import Submission


class SubmissionRepository:
    def get_submission_by_id(self, quiz_submission_id: str) -> Submission:
        return Submission.objects.get(quiz_submission_id=quiz_submission_id)

    def get_submission_by_user_and_quiz(self, user_id: str, quiz_id: str) -> Submission:
        return Submission.objects.get(user_id=user_id, quiz_id=quiz_id)

    def save_submission(self, submission: Submission) -> Submission:
        submission.save()
        return submission

    def delete_submission(self, quiz_submission_id: str) -> None:
        Submission.objects.filter(
            quiz_submission_id=quiz_submission_id).delete()
