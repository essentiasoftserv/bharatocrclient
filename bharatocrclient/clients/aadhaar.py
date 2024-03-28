import requests as re
from bharatocrclient.clients.common import get_full_path


def parse_aadhaar_card(key, front_image_path, back_image_path):
    url = get_full_path("aadhaar")
    files = {
        "front_side": open(front_image_path, "rb"),
        "back_side": open(back_image_path, "rb"),
    }
    headers = {"Authorization": f"Bearer {key}"}
    return re.post(url=url, files=files, headers=headers).json()


def aadhaar(key, front_image_path, back_image_path):
    return parse_aadhaar_card(key, front_image_path, back_image_path)
