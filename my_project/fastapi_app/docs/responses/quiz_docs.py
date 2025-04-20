from fastapi_app.schemas.quiz_schema import QuizListItemSchema, QuizDetailResponse
from ..common_docs import SuccessResponse
from fastapi_app.docs.error_docs import error_docs

quiz_detail_docs = {
    "response_model": SuccessResponse[QuizDetailResponse],
    "responses": {
        200: {
            "description": "퀴즈 상세 조회 성공",
            "content": {
                "application/json": {
                    "example": {
                        "message": "퀴즈 조회 성공",
                        "data": {
                            "quiz_id": "3fd5e6b1-0c97-41ef-94b3-4abcf53a8dc6",
                            "title": "Python 기초 퀴즈",
                            "description": "객체지향과 관련된 개념을 테스트하는 문제들",
                            "page": 1,
                            "total_pages": 3,
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

quiz_list_docs = {
    "response_model": SuccessResponse[list[QuizListItemSchema]],
    "responses": {
        200: {
            "description": "퀴즈 목록 조회 성공",
            "content": {
                "application/json": {
                    "example": {
                        "message": "퀴즈 목록 조회 성공",
                        "data": [
                            {
                                "quiz_id": "abf7d7b5-d8fd-4b6f-bf91-6ef30e6ea931",
                                "title": "Python 기초 퀴즈",
                                "description": "기초 문법 확인",
                                "created_by": "admin",
                                "has_submitted": False
                            },
                            {
                                "quiz_id": "4de38a6e-514d-4f86-92a6-9204829d3d5a",
                                "title": "Django 모델 퀴즈",
                                "description": "ORM 사용 능력 테스트",
                                "created_by": "admin",
                                "has_submitted": True
                            }
                        ]
                    }
                }
            }
        },
        **error_docs
    },
}
