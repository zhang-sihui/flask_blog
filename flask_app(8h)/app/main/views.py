from datetime import datetime
from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())
