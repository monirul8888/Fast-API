from fastapi import FastAPI, Path, HTTPException
import json
from pydantic_app import BaseModel


app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return{"message" : "Hello World"}

@app.get("/about")
def about():
    return {"message" : "Monirul Islam"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/view/{patient_id}")
def view(patient_id: int):

    data = load_data()
    for patient in data:
        if patient["id"] == patient_id:
            return patient
    raise HTTPException(status_code=404, detail= "Patient Not Exists")
    
    
class Patients(BaseModel):
    name: str
    age: int

def insert(patient: Patients):
    print(patient.name)
    print(patient.age)
    print("Inserted Successfully")


patient_info = {"name": "Monirul",
                "age": 25}

patient1 = Patients(**patient_info)


