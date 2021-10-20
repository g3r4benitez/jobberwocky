from dependency_injector import containers, providers
from app.services.job_service import JobService


class ContainerService(containers.DeclarativeContainer):
    job_service = providers.Singleton(
        JobService
    )