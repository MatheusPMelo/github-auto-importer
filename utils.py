import os
import subprocess

def system(command) :
    return os.system(command)

def isInstalled(dependency):
    try:
        subprocess.check_output(['which', dependency])
        return True
    except subprocess.CalledProcessError:
        print(f"O programa {dependency} não está instalado no sistema.")
        return False