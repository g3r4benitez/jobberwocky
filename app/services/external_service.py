import requests

from app.core.config import EXTERNAL_SOURCE_URL


class ExternalService:
    @staticmethod
    def get_jobs(job_title, country, salary_min, salary_max):
        """Get a contact from bitrix"""
        params = ExternalService.define_parameters(country, job_title, salary_max, salary_min)
        job_list = requests.get(EXTERNAL_SOURCE_URL, params=params)
        return job_list.json()

    @staticmethod
    def define_parameters(country, job_title, salary_max, salary_min):
        params = {}
        if job_title:
            params['name'] = job_title
        if country:
            params['country'] = country
        if salary_min:
            params['salary_min'] = salary_min
        if salary_max:
            params['salary_max'] = salary_max
        return params


external_service = ExternalService()
