from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def about():
    return {"message" : "Welcome To Fast API"}