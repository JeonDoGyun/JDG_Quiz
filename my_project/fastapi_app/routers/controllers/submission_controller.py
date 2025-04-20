from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.responses import JSONResponse

from ...schemas.submission_schema import AnswerSubmissionRequest, SubmissionResultResponse
from ...docs.responses.submission_docs import submission_init_docs, submit_answer_docs, submission_result_docs
from ..dependencies.submission_dependency import get_submission_service
from ..dependencies.quiz_dependency import get_current_user_id

from django_app.submission.services.submission_service import SubmissionService

router = APIRouter(prefix="/submissions", tags=["Submissions"])


# 응시 시작
@router.post("/init/{quiz_id}", **submission_init_docs)
def init_submission(
    quiz_id: int = Path(..., description="응시할 퀴즈 ID"),
    user_id: str = Depends(get_current_user_id),
    submission_service: SubmissionService = Depends(get_submission_service),
):
    submission = submission_service.create_submission(user_id, quiz_id)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Submission initialized",
                 "submission_id": str(submission.id)}
    )


# 응시 후 답안 제출 + 채점
@router.post("/{submission_id}/answers", **submit_answer_docs)
def submit_answers(
    submission_id: str,
    payload: AnswerSubmissionRequest,
    user_id: str = Depends(get_current_user_id),
    submission_service: SubmissionService = Depends(get_submission_service),
):
    submission = submission_service.get_submission_by_id(submission_id)
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    updated_submission = submission_service.submit_answers(
        submission=submission,
        user_id=user_id,
        answers_data=[answer.model_dump_json() for answer in payload.answers]
    )

    return {
        "message": "Answers submitted and graded",
        "submission_id": str(updated_submission.quiz_submission_id),
        "score": updated_submission.score,
        "submitted_at": updated_submission.submitted_at.isoformat()
    }


# 응시 결과
@router.get("/{submission_id}/result", response_model=SubmissionResultResponse, **submission_result_docs)
def get_submission_result(
    submission_id: str,
    user_id: str = Depends(get_current_user_id),
    submission_service: SubmissionService = Depends(get_submission_service),
):
    try:
        submission = submission_service.get_submission_result(
            submission_id, user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Submission not found")
    except PermissionError:
        raise HTTPException(status_code=403, detail="Access denied")

    return SubmissionResultResponse(
        submission_id=str(submission.id),
        score=submission.score,
        submitted_at=submission.submitted_at,
        message="Submission result retrieved successfully"
    )
