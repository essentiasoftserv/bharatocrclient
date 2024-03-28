DOMAIN = "api.essentiasoftserv.com"


def get_api_url():
    return f"https://{DOMAIN}/api/v1/"


def get_full_path(feature_path):
    return f"{get_api_url()}{feature_path}"
