from pydantic import BaseModel
from typing import list, Dict, Optional


class Patient(BaseModel):
    name:str
    age: int
    weight: float
    married : bool = False 
    allergies: Optional[list[str]] = None
    contact_details : Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('updated')    

patient_info = {'name':'sarang','age': '23', 'weight':62.3, 'married':'true',
              'allergies':['pollen','dust']}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)
