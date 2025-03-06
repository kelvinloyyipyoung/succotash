from flask import Flask, render_template
from static.projects.projects import PROJECTS

app = Flask(__name__)

@app.route('/')
def index():
    title = "Hello, I'm Kelvin."
    title_2 = "I'm a developer."
    body = "I make random tools and put them on this website."
    context = PROJECTS
    return render_template('index.html', title=title, title_2=title_2, body = body, context = context)

@app.route('/about')
def about():
    title = "I make random tools and put them on this website."
    body = "This website is basically a graveyard for all the random ideas I get and decide to build with Python.  It all started back in uni when I first learned the language. Something about its simplicity and versatility just clicked with me, and now it's my go-to for pretty much everything.  So, here you'll find a bunch of projects that probably don't have much in common except that they were all built by me (and with Python, of course)."
    body_2 = "Some of them might be useful, some might be just plain silly, but they all represent something I learned or experimented with along the way.  If you're curious about the code, feel free to poke around. And if you have any thoughts or questions, I'm always up for a chat about coding, bad ideas, or anything else that comes to mind."
    return render_template('about.html', title=title, body=body, body_2=body_2)

@app.route('/contact')
def contact():
    title = "I'm looking for a job."
    body = "If you have any opportunities, please contact me at:"
    contact_info = {
        "Phone": "0406 815 094",
        "Email": "kelvinloyyipyoung@gmail.com",
    }
    links = {        
        "GitHub": "https://github.com/kelvinloyyipyoung",
        "LinkedIn": "https://linkedin.com/in/kelvinloyyipyoung"
    }
    return render_template('contact.html', title=title, body=body, contact_info=contact_info, links=links)

if __name__ == '__main__':
    app.run(debug=True)