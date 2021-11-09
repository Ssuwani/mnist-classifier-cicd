import os
import requests
from github import Github

def trigger_dispatch(ACCESS_TOKEN):
    print("ACCESS_TOKEN: ", ACCESS_TOKEN)
    g = Github(ACCESS_TOKEN)
    g.get_user("ssuwani").get_repo("mnist-classifier-cicd").create_repository_dispatch("FINISH_TRAINING")
    
    print("Trigger CD workflow")

