import os
import requests
from github import Github

def trigger_dispatch(ACCESS_TOKEN):

    github_token = ACCESS_TOKEN
    g = Github(github_token)
    g.get_user("ssuwani").get_repo("mnist-classifier-cicd").create_repository_dispatch("FINISH_TRAINING")
    
    print("Trigger CD workflow")

