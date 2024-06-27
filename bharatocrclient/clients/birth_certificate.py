import requests as re
from bharatocrclient.clients.common import get_full_path


def parse_birth_certificate(key, image_path):
    url = get_full_path("birth-certificate")
    files = {"image": open(image_path, "rb")}
    headers = {"Authorization": f"Bearer {key}"}
    return re.post(url=url, files=files, headers=headers).json()


def birth_certificate(key, image_path):
    return parse_birth_certificate(key, image_path)
