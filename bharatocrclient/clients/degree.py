import requests as re
from bharatocrclient.clients.common import get_full_path


def parse_degree(key, image_path):
    url = get_full_path("degree")
    files = {"image": open(image_path, "rb")}
    headers = {"Authorization": f"Bearer {key}"}
    return re.post(url=url, files=files, headers=headers).json()


def degree(key, image_path):
    return parse_degree(key, image_path)
