from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"welcome to fastapi"}

# Lesson - 1
@app.get("/health")
def hello():
    return {"health": "Ok"}
# @app.get("/health")
# def hello():
#     return {"health": "Ok"}

@app.get("/greet/{name}")
def greet(name:str):
    return {"name":name}
# @app.get("/greet/{name}")
# def greet(name: str):
#     return {"message": f"Hello, {name}!"}

@app.get("/square/{number}")
def sqr(number:int):
    return {"Square":number**2}
# @app.get("/square/{number}")
# def calculate_square(number: int):
#     return {
#         "number": number,
#         "square": number ** 2
#     }