import app.repositories.job_repository as job_repo

from app.models.job import Job


class JobService:
    @staticmethod
    def create(job: Job):
        """Create a new job in local db"""
        job_obj = job_repo.create(job)
        return job_obj

    @staticmethod
    def search_jobs(job_title):
        """Search jobs in local and external sources"""
        job_list = []
        jobs = job_repo.search(job_title)
        for j in jobs:
            job_list.append({
                'name': j.name,
                'salary': j.salary,
                'country': j.country,
                'skills': j.skills
            })

        return job_list

    @staticmethod
    def list():
        """
        a complete list of local jobs
        """
        jobs = job_repo.get_list()
        return jobs

