import requests as re
from bharatocrclient.clients.common import get_full_path


def parse_vehicle_registration(key, image_path):
    url = get_full_path("vehicle-registration")
    files = {"image": open(image_path, "rb")}
    headers = {"Authorization": f"Bearer {key}"}
    return re.post(url=url, files=files, headers=headers).json()


def vehicle_registration(key, image_path):
    return parse_vehicle_registration(key, image_path)
