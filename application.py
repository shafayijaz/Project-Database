from cs50 import SQL
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///DB-Proj.db")

@app.route("/")
def index():
    return render_template("index.html")

# Gives options for update, view & Delete
@app.route("/school")
def school():
    return render_template("school/School.html")

# Handles the url
@app.route("/handleSchool", methods=["POST", "GET"])
def handleSchool():
    if request.form["button"] == "schoolView":
        return redirect(url_for("schoolView"))
    elif request.form["button"] == "schoolDelete":
        return redirect(url_for("schoolDelete"))
    elif request.form["button"] == "InsSchool":
        return redirect(url_for("InsSchool"))

# renders a new html file
@app.route("/InsSchool")
def InsSchool():
    return render_template("school/InsSchool.html")

# deals with updation of the table
@app.route("/schoolInsert", methods=["POST"])
def schoolInsert():
    if request.form["Sname"] == "" or request.form["Location"] == "":
        return render_template("failure.html")
    db.execute("INSERT INTO School(Sname, Location, PhoneNo, Website) VALUES(:Sname, :Location, :PhoneNo, :Website)",
        Sname=request.form["Sname"], Location=request.form["Location"], PhoneNo=request.form["PhoneNo"], Website=request.form["Website"])
    return render_template("success.html")

# deals with View of the table
@app.route("/schoolView")
def schoolView():
    rows = db.execute("SELECT * FROM School")
    return render_template("school/schoolView.html", schoolView = rows)

# deals with Deletion of the table
@app.route("/schoolDelete", methods= ["GET", "POST"])
def schoolDelete():
    if request.method == "GET":
        rows = db.execute("SELECT * FROM School")
        return render_template("school/schoolDelete.html", schoolDelete= rows)
    elif request.method == "POST":
        if request.form["RegNo"]:
            db.execute("DELETE FROM School WHERE RegNo = :RegNo",RegNo=request.form["RegNo"])
        return redirect(url_for("schoolView"))