import json

from app import app, login_manager

from flask import Flask, request, render_template, redirect, url_for, flash
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin,
                            confirm_login, fresh_login_required)
 
class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active
 
    def is_active(self):
        return self.active

USERS = {
    1: User(u"Damian", 1),
    2: User(u"Damian2", 2, False)
}
 
USER_NAMES = dict((u.name, u) for u in USERS.itervalues())
 

 
@login_manager.user_loader
def load_user(id):
    return USERS.get(int(id))
 
 
@app.route("/secret")
@fresh_login_required
def secret():
    return render_template("secret.html")
 
 
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST" and "username" in request.form:
        username = request.form["username"]
        if username in USER_NAMES:
            remember = request.form.get("remember", "no") == "yes"
            if login_user(USER_NAMES[username], remember=remember):
                flash("Logged in!")
                return redirect(request.args.get("next") or url_for("index"))
            else:
                flash("Sorry, but you could not log in.")
        else:
            flash(u"Invalid username.")
    return render_template("login.html",layout = 'layout_default.html')
 
 
@app.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    if request.method == "POST":
        confirm_login()
        flash(u"Reauthenticated.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("reauth.html")
 
 
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))
