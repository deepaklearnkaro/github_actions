from fastapi import FastAPI

app = FastAPI(title="FastAPI Auto Deploy Demo")

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "FastAPI deployed using GitHub Actions 🚀"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
