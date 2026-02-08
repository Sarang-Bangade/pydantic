# Field validation in pydantic 
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List , Dict , Optional, Annotated

class Patient(BaseModel):

    name:str
    email:EmailStr
    age : int
    weight : float
    married :bool
    allergies : List[str]
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

patient_info = {'name':'Sarang','email':'abc@gmail.com' ,'age':23, 'weight':'75.2','married':True, 'allergies':[], 'contact_details':{'email':'abc@gmail.com','phone':'23456789'}}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)
