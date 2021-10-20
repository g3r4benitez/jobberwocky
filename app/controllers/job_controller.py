from fastapi import APIRouter, Security, Depends
from dependency_injector.wiring import inject, Provide
from starlette import status

from app.models.job import Job
from app.services.job_service import JobService
from app.services.external_service import ExternalService
from app.core.containers import ContainerService

router = APIRouter()


@router.post(
    "",
    name="job_create",
    status_code=status.HTTP_201_CREATED,
    response_model=Job,
)
@inject
async def post_create(
        job: Job,
        job_service: JobService = Depends(Provide[ContainerService.job_service]),
):
    return job_service.create(job)

@router.post(
    "/search",
    name="search_jobs",
    status_code=status.HTTP_200_OK,
)
@inject
def search_jobs(
        job_title: str,
        job_service: JobService = Depends(Provide[ContainerService.job_service]),
):
    job_list = job_service.search_jobs(job_title)
    external_list = ExternalService.get_jobs(job_title)
    job_list.extend(external_list)
    return job_list

@router.get(
    "/list",
    name="job_list",
    status_code=status.HTTP_200_OK,
)
@inject
def get_list(
        job_service: JobService = Depends(Provide[ContainerService.job_service]),
):
    return job_service.list()


