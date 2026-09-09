from fastapi import FastAPI

app = FastAPI(title="cd-vyral-system")


@app.get("/")
def read_root():
    return {"message": "cd-vyral-system is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
