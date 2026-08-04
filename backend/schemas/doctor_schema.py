from pydantic import BaseModel


class DoctorBase(BaseModel):
    first_name: str
    last_name: str
    specialization: str
    phone: str
    email: str
    experience: int


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True