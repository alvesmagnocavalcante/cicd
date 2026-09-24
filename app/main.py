from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CI/CD funcionando!"}


@app.get("/health")
def health():
    return {"status": "ok"}