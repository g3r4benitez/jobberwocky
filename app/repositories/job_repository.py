from fastapi_sqlalchemy import db

from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_, or_
from app.models import job as models
from app.models.orm import job as orm
from app.exceptions.job_exceptions import NotFound


def get_by_id(id: int):
    with db():
        obj_job = db.session.query(orm.Job).get(id)
        if obj_job:
            return obj_job
        raise NotFound()


def update(job: orm.Job):

    db.session.merge(job)
    db.session.commit()


def create(job: models.Job):
    """Create an Impo on db if it has not been created before."""
    with db():
        entity = orm.Job(**job.dict())
        db.session.add(entity)
        db.session.commit()
        db.session.refresh(entity)
        db.session.expunge(entity)
        return entity


def search(job_title: str = None, country: str = None, salary_min: float = None, salary_max: float = None):
    """search jobs"""
    with db():
        job_list = db.session.query(orm.Job)
        if job_title:
            job_list = job_list.filter(orm.Job.name.like(f'%{job_title}%'))
        if country:
            job_list = job_list.filter(orm.Job.country.like(f'%{country}%'))
        if salary_min:
            job_list = job_list.filter(orm.Job.salary >= salary_min)
        if salary_max:
            job_list = job_list.filter(orm.Job.salary <= salary_max)

        return job_list


def get_list():
    """Return a list of jobs"""
    with db():
        return db.session.query(orm.Job).all()

