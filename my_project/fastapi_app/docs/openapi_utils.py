from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
      
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    
    openapi_schema["externalDocs"] = {
        "description": "📘 관리자용 DRF Swagger 문서 보기",
        "url": "http://localhost/internal/drf-docs/"  # nginx를 통해 매핑된 경로 기준
    }
    
    app.openapi_schema = openapi_schema
    
    return app.openapi_schema