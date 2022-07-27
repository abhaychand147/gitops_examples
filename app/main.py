from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def print_item():
    return {"Hello:World!"}

@app.get("/first")
def first():
    return {"First:API"}


