from fastapi import FastAPI

app = FastAPI()

# uvicorn fastapi_app.main:app --reload 

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}
