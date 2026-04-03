from pydantic import BaseModel
from typing import List, Dict, Optional
class Patients (BaseModel):
    name: str
    age: int
    married: Optional[bool]= False
    alergics: Optional[List [str]] = None
    contact : Dict [str, str]


def insert(patient: Patients):
    print(patient.name)
    print(patient.age)
    print(patient.alergics)
    print(patient.contact)
    print("Inserted Successfully")

patient_info = {"name": "Monirul",
                "age": 25,
                "married": False,
                "contact":{
                    "Phone": "01742958888",
                    "Email": "monirul.cr3@gmail.com"
                }
                }

patient1 = Patients(**patient_info)
insert(patient1)