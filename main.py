from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Inbox Agent backend is running"}
