
from pydantic import BaseModel
from typing import List , Dict , Optional
class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool = False
    allergies:Optional[List[str]]=None #for 2level validity we use list.The inner content is also string in the ['string','string']
    contact_details: Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('updated')    

patient_info = {'name':'Sarang', 'age':23, 'weight':75.2,'married':True, 'allergies':[], 'contact_details':{'email':'abc@gmail.com','phone':'23456789'}}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)
