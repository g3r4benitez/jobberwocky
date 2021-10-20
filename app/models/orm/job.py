from sqlalchemy import Column, Float, Integer, String
from app.models.orm import Base


class UpdateMixin:
    """Add a simple update() method to instances that accepts
    a dictionary of updates.
    """
    def update(self, values):
        for k, v in values.items():
            setattr(self, k, v)


class Job(Base, UpdateMixin):
    __tablename__: str = "job"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(100), index=True)
    country = Column(String(2), index=True)
    salary = Column(Float)
    skills = Column(String(255), index=False)

    @property
    def _skills(self):
        return self.skills.replace(",", "").split()
