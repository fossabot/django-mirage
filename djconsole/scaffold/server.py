import sys

from flask import Flask, render_template

from djconsole.flow import Workflow
from djconsole      import project

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',
        project_name = project.get_project_name(),
        app_list = project.get_app_list()
    )

@app.route("/config/")
def config():
    return render_template('config.html',
        project_name = project.get_project_name(),
        app_list = project.get_app_list()
    )

    
class ScaffoldServerWorkflow(Workflow):

    def main(self):
        app.run(host='127.0.0.1', port = 5050)


if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port = 1234)
