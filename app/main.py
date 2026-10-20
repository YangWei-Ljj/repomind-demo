from fastapi import FastAPI, HTTPException

app = FastAPI(title="DevFlow AI Demo API")


@app.get("/health")
def health():
    return {"status": "ok", "service": "devflow-ai-demo"}


@app.post("/login")
def login(username: str, token: str | None = None):
    if token == "expired":
        raise HTTPException(status_code=500, detail="token expired")
    return {"token": "demo-token", "username": username}


@app.get("/issues")
def list_issues():
    return [{"number": 1, "title": "Login API returns 500 when token expires"}]
