from pydantic import BaseModel, Field, condecimal


class Job(BaseModel):
    name: str = Field("Name")
    country: str = Field("Country")
    salary: str = Field("Salary")
    skills: str = Field("List of skills")

    class Config:
        orm_mode = True
