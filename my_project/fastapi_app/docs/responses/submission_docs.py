from fastapi_app.schemas.submission_schema import (
    SubmissionInitResponse,
    SubmissionResultResponse,
)
from ..common_docs import SuccessResponse
from fastapi_app.docs.error_docs import error_docs

submission_init_docs = {
    "response_model": SuccessResponse[SubmissionInitResponse],
    "responses": {
        200: {
            "description": "응시 시작 및 문제 제공 성공",
            "content": {
                "application/json": {
                    "example": {
                        "message": "응시가 시작되었습니다.",
                        "data": {
                            "submission_id": "e91f21c7-a2d6-41a2-9147-f15778f5eb4e",
                            "quiz_id": "3fd5e6b1-0c97-41ef-94b3-4abcf53a8dc6",
                            "questions": [
                                {
                                    "question_id": "82cf7b1a-e78d-47c9-bfa2-cc703d9e92c6",
                                    "description": "다음 중 파이썬의 키워드가 아닌 것은?",
                                    "choices": [
                                        {"choice_id": "1", "text": "lambda"},
                                        {"choice_id": "2", "text": "yield"},
                                        {"choice_id": "3", "text": "function"},
                                        {"choice_id": "4", "text": "def"}
                                    ]
                                }
                            ]
                        }
                    }
                }
            }
        },
        **error_docs,
    },
}


submit_answer_docs = {
    "response_model": SuccessResponse[dict],
    "responses": {
        200: {
            "description": "답안 제출 성공",
            "content": {
                "application/json": {
                    "example": {
                        "message": "답안이 성공적으로 제출되었습니다.",
                        "data": {
                            "submission_id": "e91f21c7-a2d6-41a2-9147-f15778f5eb4e"
                        }
                    }
                }
            }
        },
        **error_docs,
    },
}


submission_result_docs = {
    "response_model": SuccessResponse[SubmissionResultResponse],
    "responses": {
        200: {
            "description": "제출 결과 조회 성공",
            "content": {
                "application/json": {
                    "example": {
                        "message": "제출 결과 조회 성공",
                        "data": {
                            "score": 7,
                            "total": 10,
                            "correct_choices": [
                                "e325b7c3-f1ad-47e1-a4e9-d5c19b8571f5",
                                "fa7c3c5d-2c83-41e6-90e3-8fdd0dc8a61f"
                            ]
                        }
                    }
                }
            }
        },
        **error_docs,
    },
}
