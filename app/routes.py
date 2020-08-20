from flask import render_template, url_for, request
from app import app
from app.forms import DatabaseForm, ClassifierForm
import time

@app.route("/", methods=["GET","POST"])
def index():
    while True:
        form = ClassifierForm()
        return render_template("base.html", title="Classifier", form=form)
