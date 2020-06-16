import os
import subprocess
import platform

def run_app():
    os.chdir('joshguarino')
    if platform.system() == 'Windows':
        subprocess.call(["py", "app.py"])
        return
    subprocess.call(["python3", "app.py"])

def dep_install():
    subprocess.call(["pipenv", "install"])   

if __name__ == '__main__':
    dep_install()
    run_app()