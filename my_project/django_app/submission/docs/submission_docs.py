from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

answer_submit_docs = swagger_auto_schema(
    operation_summary="퀴즈 응답 제출",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'answers': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'question_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'selected_choice_id': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        },
        example={
            "answers": [
                {"question_id": 1, "selected_choice_id": "abc123"},
                {"question_id": 2, "selected_choice_id": "def456"}
            ]
        }
    ),
    responses={
        200: openapi.Response(
            description="제출 완료",
            examples={
                "application/json": {
                    "submission_id": "uuid",
                    "score": 2,
                    "submitted_at": "2024-01-01T12:00:00",
                    "message": "퀴즈 제출이 완료되었습니다."
                }
            }
        ),
        400: openapi.Response(description="잘못된 요청 형식"),
        403: openapi.Response(description="권한 없음 (사용자 전용)")
    }
)
