from fastapi import FastAPI

app = FastAPI(title="Furnishop Demo API")


@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to Furnishop API"}
