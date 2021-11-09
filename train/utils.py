import os
import requests


def trigger_dispatch(ACCESS_TOKEN):

    OWNER = "ssuwani"
    REPO = "mnist-classifier-cicd"
    VERSION = "v1"

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {ACCESS_TOKEN}",
    }

    data = {
        "event_type": "FINISH_TRAINING",
        "client_payload": {
            "version": VERSION
        }
    }

    requests.post(
        f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches",
        data=data,
        headers=headers
    )
    print("Trigger CD workflow")