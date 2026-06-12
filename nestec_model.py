from pydantic import BaseModel
class Address(BaseModel):
    state:str
    state:str
    pin:str

class Patient(BaseModel):
    name: str
    gender:str
    age:int
    address: Address

address_dict ={'city':'nagpur', 'state':'maharashtra', 'pin':'40034'} 
address1 = Address(**address_dict)

patient_dict = { 'name':'sarang', 'gender':'male','age':23,'address':address1}
patient1 = Patient(**patient_dict)
print(patient1)
temp = patient1.model_dump(exclude=['name','gender'])
print(temp)
print(type(temp))