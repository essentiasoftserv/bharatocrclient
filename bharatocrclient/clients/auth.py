import requests as re
import time
import json
import random

from bharatocrclient.clients.exceptions import (
    UnableToLoginClientError,
    UnableToRegisterError,
    InvalidFileType,
    InvalidFilePath,
    UnableToUpdatePermissionsClientError,
)
from bharatocrclient.clients.common import get_full_path


def process_login(email, password, try_number):
    try:
        url = get_full_path("auth/login")
        data = {"email": email, "password": password}
        response = re.post(url, json=data)
        if response.status_code == 200:
            return response.json()["auth_token"], response.status_code
        else:
            return None, response.status_code
    except (
        re.exceptions.ConnectionError,
        json.decoder.JSONDecodeError,
    ) as ex:
        if try_number == 3:
            raise UnableToLoginClientError
        time.sleep(random.random() * 2)
        return process_login(url, data, try_number=try_number + 1)


def login(email, password):
    return process_login(email, password, 1)


def process_register(email, password, full_name, use_type, try_number):
    try:
        url = get_full_path("auth/register")
        data = {
            "email": email,
            "password": password,
            "full_name": full_name,
            "use_type": use_type,
        }
        response = re.post(url, json=data)
        if response.status_code == 201:
            return response.status_code
        else:
            return response
    except (
        re.exceptions.ConnectionError,
        json.decoder.JSONDecodeError,
    ) as ex:
        if try_number == 3:
            raise UnableToLoginClientError
        time.sleep(random.random() * 2)
        return login(url, data, try_number=try_number + 1)
    else:
        return res_json


def register(email, password, full_name, use_type):
    return process_register(email, password, full_name, use_type, 1)
