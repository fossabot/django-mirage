from console import command
from os import chdir
from shutil import move
from console import log
from projectstartup.readme import create_readme_doc

def dj_new_flow(name = None):
    if name == None:
        log("Please type your new Django application name.")
        name = log("App Name", withInput = True)

    _create_new_django_app(name)

    chdir("./" + name)
    _create_template_git_project(name)
    _create_docs(name)


def _create_new_django_app(name):
    command("django-admin startproject " + name)


def _create_template_git_project(name):
    command("curl -O https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore")
    move("Python.gitignore", ".gitignore")
    command("git init")

def _create_docs(name):
    with open("README.md", "a") as readme:
        readme.write(create_readme_doc(name))
