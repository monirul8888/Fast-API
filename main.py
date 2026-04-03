from fastapi import FastAPI
import json

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
    return{"error" : "ID not found"}
    
    
    