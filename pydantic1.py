
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List , Dict , Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the Patient',description='Give the name of patient in less than 50 chars',examples=['Nitish','Amit'])]
    email:EmailStr
    linkedin_url :AnyUrl
    age:int = Field(gt=0,lt=20)
    weight:Annotated[float , Field(gt=0, strict = True)]
    married : Annotated[bool, Field(default = None, description='Is the patient married or not')]
    allergies:Annotated[Optional[List[str]],Field(max_length = 5)] # for 2level validity we use list.The inner content is also string in the ['string','string']
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

patient_info = {'name':'Sarang','email':'abc@gmail.com' ,'age':23, 'weight':'75.2','married':True, 'allergies':[], 'contact_details':{'email':'abc@gmail.com','phone':'23456789'}}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)
