from pydantic import BaseModel, Field, condecimal


class Job(BaseModel):
    name: str = Field("Name")
    country: str = Field("Country")
    salary: condecimal(gt=0.00, decimal_places=2)
    skills: str = Field("List of skills")

    class Config:
        orm_mode = True


