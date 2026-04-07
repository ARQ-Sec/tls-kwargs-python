import requests

def fetch_payload(url: str) -> str:
    return requests.get(url, verify=True, timeout=5).text
