from wtforms import StringField, BooleanField, SubmitField, SelectField, FileField, IntegerField
from wtforms.fields.html5 import IntegerRangeField
from flask_wtf import FlaskForm
from pathlib import Path
class ClassifierForm(FlaskForm):
    select_class = SelectField("Classifier model",
            choices = [("knn","K-Nearest Neighbors"),
                       ("svm","Suport Vector Machine"),
                       ("tree","Decision Tree")],
            render_kw = {"onchange": "updateClassifier()"})

    fit = SubmitField("Fit")

class KNNForm(FlaskForm):

    n_neighbors = IntegerField("Number of neighbors: ")
    weights = SelectField("")

class DatabaseForm(FlaskForm):
    browse = FileField("Select data file: ")
    split = IntegerRangeField("Split data: ")
