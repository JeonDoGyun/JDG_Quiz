from my_project.fastapi_app.docs.common_docs import ErrorResponse

error_docs = {
    400: {"model": ErrorResponse, "description": "잘못된 요청입니다."},
    403: {"model": ErrorResponse, "description": "권한이 없습니다."},
    404: {"model": ErrorResponse, "description": "리소스를 찾을 수 없습니다."},
    500: {"model": ErrorResponse, "description": "서버 내부 오류"},
}
