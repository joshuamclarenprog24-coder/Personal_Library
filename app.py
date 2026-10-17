from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

title_bar = {
        1: {"text":"UBIBLIO", "class": "brand"},
        2: {"text":"PERSONAL LIBRARY", "class": "title"},
        3: {"text":"Menu ☰", "class" : "menu"},
}

buttons = {
        1: {"text":"SEARCH", "class": "btn-search"},
        2: {"text":"ADD NEW", "class": "btn-add-new"},
        3: {"text":"SHOWN WITHDRAWN", "class" : "btn-show-WITHDRAWN"},
}

class Books(db.Model):
    __tablename__ = 'Books'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64), unique=True)
    author = db.Column(db.String(64), unique=False)
    completed = db.Column(db.String(3), unique=False)
    review = db.Column(db.String(64), unique = True) 

    def __repr__(self):
        return '<Title%r>' % self.title

@app.route('/')
def index():
    books = Books.query.all()
    return render_template('index.html', 
                           title_bar=title_bar,
                           buttons=buttons, 
                           books=books)
