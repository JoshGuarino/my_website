import os
import subprocess

def run_app():
    os.chdir('joshguarino')
    subprocess.call(["py", "app.py"])

def dep_install():
    subprocess.call(["pipenv", "install"])   

if __name__ == '__main__':
    dep_install()
    run_app()