import requests
from django.conf import settings


class ConnectService:
    @classmethod
    def service(
            cls,
            url: str,
            method: str,
            params: dict = {},
            headers: dict = {},
            body: dict = {},
    ):
        kwargs = {
            "url": settings.API_URL + url,
            "method": method,
        }

        headers = {
            "Authorization": settings.KEY,
        }

        if isinstance(params, dict) and params:
            kwargs["params"] = params
        if isinstance(headers, dict) and headers:
            kwargs["headers"] = headers
        if isinstance(body, dict) and body:
            kwargs["json"] = body

        response = requests.request(**kwargs)
        response.raise_for_status()  # Генерирует исключение, если статус код не 200
        return response.json()
