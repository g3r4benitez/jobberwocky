from fastapi import APIRouter

from app.controllers import job_controller as router_job
from app.core.config import API_PREFIX

api_router = APIRouter(prefix=API_PREFIX)
api_router.include_router(router_job.router, tags=["job"], prefix="/job")
