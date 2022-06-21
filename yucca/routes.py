from flask import render_template, url_for, request, redirect, session, flash
# from yucca.forms import RegistrationForm, LoginForm, ConsentForm
# from yucca.models import Account, StudyEntry
import yucca.utils as ut
from yucca import app, db, bcrypt
# from yucca import login_user, current_user, logout_user


@app.route('/')
def home():
    return render_template("home.html")

