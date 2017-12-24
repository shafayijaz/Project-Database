from cs50 import SQL
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///DB-Proj.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/school")
def school():
    return render_template("School.html")

@app.route("/handleSchool", methods=["POST"])
def handleSchool():
    if request.form["button"] == "schoolView":
        return schoolView()
    elif request.form["button"] == "schoolDelete":
        return schoolDelete()
    elif request.form["button"] == "InsSchool":
        return InsSchool()

@app.route("/InsSchool")
def InsSchool():
    return render_template("InsSchool.html")

@app.route("/schoolInsert", methods=["POST"])
def schoolInsert():
    if request.form["Sname"] == "" or request.form["Location"] == "":
        return render_template("failure.html")
    db.execute("INSERT INTO School(Sname, Location, PhoneNo, Website) VALUES(:Sname, :Location, :PhoneNo, :Website)",
        Sname=request.form["Sname"], Location=request.form["Location"], PhoneNo=request.form["PhoneNo"], Website=request.form["Website"])
    return render_template("success.html")

@app.route("/schoolView")
def schoolView():
    rows = db.execute("SELECT * FROM School")
    return render_template("schoolView.html", schoolView = rows)

@app.route("/schoolDelete", methods= ["GET", "POST"])
def schoolDelete():
    if request.method == "GET":
        rows = db.execute("SELECT * FROM School")
        return render_template("schoolDelete.html", schoolDelete= rows)
    elif request.method == "POST":
        if request.form["RegNo"]:
            db.execute("DELETE FROM School WHERE RegNo = :RegNo",RegNo=request.form["RegNo"])
        return redirect(url_for("schoolView"))