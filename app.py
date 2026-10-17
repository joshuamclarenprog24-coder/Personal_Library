from flask import Flask, render_template

app = Flask(__name__)

title_bar = {
        1: {"text":"UBIBLIO", "class": "brand"},
        2: {"text":"PERSONAL LIBRARY", "class": "title"},
        3: {"text":"Menu ☰", "class" : "menu"},
}

buttons = {
        1: {"text":"SEARCH", "class": "btn-search"},
        2: {"text":"PERSONAL LIBRARY", "class": "btn-add-new"},
        3: {"text":"SHOWN WITHDRAWN", "class" : "btn-show-WITHDRAWN"},
}

@app.route('/')
def index():
    return render_template('index.html', title_bar=title_bar, buttons=buttons)
