from flask import Flask, render_template
from static.content.content import CONTENT
from static.content.projects import PROJECTS

app = Flask(__name__)

@app.route('/')
def index():
    content = CONTENT['index']
    projects = PROJECTS
    return render_template('index.html', projects=projects, **content)

@app.route('/about')
def about():
    content = CONTENT['about']
    return render_template('about.html', **content)

@app.route('/contact')
def contact():
    content = CONTENT['contact']
    return render_template('contact.html', **content)

if __name__ == '__main__':
    app.run(debug=True)