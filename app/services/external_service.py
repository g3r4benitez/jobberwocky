import requests

from app.core.config import EXTERNAL_SOURCE_URL


class ExternalService:
    @staticmethod
    def get_jobs(job_title):
        """Get a contact from bitrix"""
        job_list = requests.get(EXTERNAL_SOURCE_URL, data={'name': job_title})
        return job_list


external_service = ExternalService()
