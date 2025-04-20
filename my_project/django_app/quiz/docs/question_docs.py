from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

question_create_docs = swagger_auto_schema(
    operation_summary="문제 등록",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'quiz_id': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'choices': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'text': openapi.Schema(type=openapi.TYPE_STRING),
                        'is_answer': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    }
                )
            )
        },
        example={
            "quiz_id": "123e4567-e89b-12d3-a456-426614174000",
            "description": "파이썬에서 리스트를 선언하는 방법은?",
            "choices": [
                {"text": "[1, 2, 3]", "is_answer": True},
                {"text": "(1, 2, 3)", "is_answer": False},
                {"text": "{1, 2, 3}", "is_answer": False}
            ]
        }
    ),
    responses={201: openapi.Response(description="문제 등록 완료")}
)
