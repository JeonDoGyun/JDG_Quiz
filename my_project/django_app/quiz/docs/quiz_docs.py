from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

quiz_create_docs = swagger_auto_schema(
    operation_summary="퀴즈 생성",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'num_questions': openapi.Schema(type=openapi.TYPE_INTEGER),
            'page_size': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
        required=['title', 'description', 'num_questions', 'page_size'],
        example={
            "title": "Python 입문 퀴즈",
            "description": "기초 문법 퀴즈입니다.",
            "num_questions": 5,
            "page_size": 2
        }
    ),
    responses={
        201: openapi.Response(
            description="퀴즈 생성 성공",
            examples={
                "application/json": {
                    "quiz_id": "123e4567-e89b-12d3-a456-426614174000",
                    "title": "Python 입문 퀴즈",
                    "description": "기초 문법 퀴즈입니다."
                }
            }
        ),
        400: openapi.Response(description="잘못된 요청 형식"),
        403: openapi.Response(description="권한 없음 (관리자 전용)")
    }
)

quiz_update_docs = swagger_auto_schema(
    operation_summary="퀴즈 수정",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'num_questions': openapi.Schema(type=openapi.TYPE_INTEGER),
            'page_size': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
        required=['title', 'description', 'num_questions', 'page_size'],
        example={
            "title": "업데이트된 퀴즈 제목",
            "description": "수정된 설명입니다.",
            "num_questions": 10,
            "page_size": 5
        }
    ),
    responses={
        200: openapi.Response(description="퀴즈 수정 성공"),
        400: openapi.Response(description="잘못된 요청 데이터"),
        404: openapi.Response(description="해당 퀴즈를 찾을 수 없음")
    }
)

quiz_delete_docs = swagger_auto_schema(
    operation_summary="퀴즈 삭제",
    responses={
        204: openapi.Response(description="삭제 성공 (응답 본문 없음)"),
        404: openapi.Response(description="삭제 대상 퀴즈를 찾을 수 없음")
    }
)
