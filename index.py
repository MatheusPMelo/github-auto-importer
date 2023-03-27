import json
from utils import *
import subprocess

with open("./repos.json") as r:
     repositories = json.load(r)

if isInstalled('gh') and isInstalled('git'):

     for repository in repositories:
        output = subprocess.check_output(["gh", "repo", "create",f"{repository['name']}", "--private"])
        url_repo_decode = output.decode("utf-8")
        system(f"git clone {repository['repository']} ./repos/{repository['name']}/")
        system(f"cd ./repos/{repository['name']} && git remote rm origin && git remote add origin {url_repo_decode}")
        system(f"cd ./repos/{repository['name']} && git branch -M main && git push -u origin main")
