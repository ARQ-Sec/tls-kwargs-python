import requests


def _transport(url: str, **kwargs) -> str:
    return requests.get(url, timeout=5, **kwargs).text


def fetch_payload(url: str) -> str:
    options = {'verify': False}
    return _transport(url, **options)
