import sys
import os
from classes.Notebook import Notebook
from modules.constants import HELP, OPTIONS_NEED_CONTENT

def go_to_projects_path():
    projects_path = os.getenv('projects_path')
    if projects_path is None:
        sys.exit('projects_path env var not configured')
    if not os.path.isdir(projects_path):
        sys.exit(f'{projects_path} is not a directory')
    os.chdir(projects_path)

def get_projects():
    go_to_projects_path()
    projects = sorted([folder for folder in os.listdir(os.curdir) if os.path.isdir(folder)])
    if not projects:
        sys.exit('No projects found')
    return projects

def get_notebooks(projects, option):
    notebooks = [Notebook(project) for project in projects]
    notebooks_w_content = [notebook for notebook in notebooks if notebook.has_content]
    if option in OPTIONS_NEED_CONTENT and not notebooks_w_content:
        sys.exit('All notebooks are empty')
    return notebooks, notebooks_w_content

def help():
    print(('\n').join(HELP))
    sys.exit(0)
