import json
from fastapi import FastAPI
from student import Student
import uvicorn
app = FastAPI()

# ================== Path Parameter ========================
# http://localhost:8000/hello/Ravi/20
@app.get("/hello/{name}/{age}")
async def hello(name:str,age:int):
   return {"name": name, "age":age}

# ================= Query Parameters =======================
# http://localhost:8000/hello?name=Ravi&age=20
@app.get("/hello")
async def hello(name:str,age:int):
   return {"name": name, "age":age}


@app.get("/")
async def hello():
   with open('a.json') as f:
      data = json.load(f)
   return data

# POST Method
@app.post("/students/")
async def student_data(s1: Student):
   return s1

if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



