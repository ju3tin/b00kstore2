#!/usr/local/bin/python3
import pymongo
import os
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Flask, render_template, url_for, flash, redirect, request, abort, session, jsonify, json
#from flask_wtf import FlaskForm
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, PasswordField
#from wtforms.validators import DataRequired
#from forms import RegistrationForm, LoginForm
#import bcrypt

# App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

	
@app.route("/")
def index ():
    todos_l = todos.find()
    return render_template('base1.html',todos=todos_l)


@app.errorhandler(404)
def page_not_found(error):
	title="error"
	return render_template('404.html', error_code='404',t=title), 404

@app.errorhandler(500)
def special_exception_handler(error):
	title="error 505"
	return render_template('500.html', error_code='500', t=title), 500
    


if __name__ == '__main__':
    app.run(debug=True)
