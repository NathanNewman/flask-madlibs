from flask import Flask, request, render_template
import stories


app = Flask(__name__)


@app.route('/home')
def load_home():
    """Displays the homepage"""
    prompts = get_prompts()
    template = get_template()
    return render_template("home.html", prompts=prompts, template=template)


def get_prompts():
    """Gets the prompts"""
    prompts = stories.story.prompts
    return prompts


def get_template():
    """Gets the template of the story"""
    template = stories.story.template
    return template


@app.route('/story', methods=['GET'])
def load_story():
    """Displays the story page"""
    answers = request.args
    text = stories.story.generate(answers)
    return render_template("story.html", text=text)
