from pydantic import BaseModel 

def UserSchema(BaseModel):
    name : str 
    username : str 
    hash_password : str 
    email : str

def UserResponseSchema(BaseModel):
    name : str 
    username : str 
    email : str
    id : int 

def LoginSchema(BaseModel):
    username : str 
    password : str 

    