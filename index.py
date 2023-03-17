import json
import os


with open("./repos.json") as r:
     repos = json.load(r)

key = 0

# Clona os repositórios em suas devidas pastas
for i in repos:

    print(i['repo_github'])

    # cria pasta para ser clonado
    os.system("mkdir ./repos/projeto{key}".format(key=key))
    
    # Fala onde é pra ser clonado
    containerRepos = './repos/projeto{key}/.'.format(key=key)

     # Clona o projeto
    os.system('git clone {gitlab} {repos}'.format(gitlab=i['repo_gitlab'], repos=containerRepos))

    # entra no diretório do projeto remove o gitlab e adiciona o git hub
    os.system('cd ./repos/projeto{key} && git remote rm origin && git remote add origin {repoGithub} && git push origin main'.format(key=key, repoGithub=i['repo_github']))

    # Incrementa 1
    key = key + 1
