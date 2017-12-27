from cs50 import SQL
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///DB-Proj.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contactUs")
def contactUs():
    return render_template("contactUs.html")

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
    db.execute("INSERT INTO School(RegNo, Sname, Location, PhoneNo, Website) VALUES(:RegNo, :Sname, :Location, :PhoneNo, :Website)",
        RegNo=request.form["RegNo"], Sname=request.form["Sname"], Location=request.form["Location"], PhoneNo=request.form["PhoneNo"], Website=request.form["Website"])
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

# COURSE
# Gives options for update, view & Delete
@app.route("/course")
def course():
    return render_template("courses/Course.html")

# Handles the url
@app.route("/handleCourse", methods=["POST", "GET"])
def handleCourse():
    if request.form["button"] == "courseView":
        return redirect(url_for("courseView"))
    elif request.form["button"] == "courseDelete":
        return redirect(url_for("courseDelete"))
    elif request.form["button"] == "InsCourse":
        return redirect(url_for("InsCourse"))

# renders a new html file
@app.route("/InsCourse")
def InsCourse():
    rows = db.execute("SELECT SchRegNo FROM Course")
    return render_template("courses/InsCourse.html", InsCourse = rows)

# deals with updation of the table
@app.route("/courseInsert", methods=["POST"])
def courseInsert():
    if request.form["CourseId"] == "" or request.form["Cname"] == "":
        return render_template("failure.html")
    db.execute("INSERT INTO Course(CourseId, Cname, Level, SchRegNo) VALUES(:CourseId, :Cname, :Level, :SchRegNo)",
        CourseId=request.form["CourseId"], Cname=request.form["Cname"], Level=request.form["Level"], SchRegNo=request.form["SchRegNo"])
    return render_template("success.html")

# deals with View of the table
@app.route("/courseView")
def courseView():
    rows = db.execute("SELECT * FROM Course")
    return render_template("courses/courseView.html", courseView = rows)

# deals with Deletion of the table
@app.route("/courseDelete", methods= ["GET", "POST"])
def courseDelete():
    if request.method == "GET":
        rows = db.execute("SELECT * FROM Course")
        return render_template("courses/courseDelete.html", courseDelete= rows)
    elif request.method == "POST":
        if request.form["CourseId"]:
            db.execute("DELETE FROM Course WHERE CourseId = :CourseId",CourseId=request.form["CourseId"])
        return redirect(url_for("courseView"))