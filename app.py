from flask import Flask, render_template, request
#from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

#debug = DebugToolbarExtension(app)

#route for questions
@app.get("/")
def index():
    """Return homepage with question form."""

    #pass variables from silly_story to HTML page
    return render_template("questions.html",prompts=silly_story.prompts)

#route for results
@app.get("/results")
def generate_story():
    """take form inputs, navigate to /results, generate and display story"""
    
    story = silly_story.generate(request.args)

    return render_template("results.html",story=story)
