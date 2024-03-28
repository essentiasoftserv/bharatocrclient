import requests as re
from bharatocrclient.clients.common import get_full_path


def parse_pan_card(key, image_path):
    url = get_full_path("pan")
    files = {"image": open(image_path, "rb")}
    headers = {"Authorization": f"Bearer {key}"}
    return re.post(url=url, files=files, headers=headers).json()


def pan(key, image_path):
    return parse_pan_card(key, image_path)
