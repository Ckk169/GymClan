from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from models.booking import Booking
from models.classes import Classes

import repositories.classes_repository as classes_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

classes_blueprint = Blueprint("classes", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/classes'
@classes_blueprint.route("/classes")
def classes():
    classes = classes_repository.select_all()
    return render_template("classes/index.html", all_classes=classes)


@classes_blueprint.route("/classes/add", methods=["GET"])
def add_classes():
    classes = classes_repository.select_all()
    return render_template("classes/add.html", all_classes=classes)


@classes_blueprint.route("/classes", methods=["POST"])
def create_classes():
    name = request.form["name"]
    size = request.form["size"]
    time = request.form["time"]

    classes = Classes(name, size, time)
    classes_repository.save(classes)
    return redirect("/classes")


@classes_blueprint.route("/classes/<id>")
def classes_page(id):
    class1 = classes_repository.select(id)
    members = classes_repository.member(class1)

    return render_template("classes/show.html", classes=class1, members=members)


@classes_blueprint.route("/classes/<id>/edit", methods=["GET"])
def edit_view_classes(id):
    classes = classes_repository.select(id)
    return render_template("/classes/edit.html", classes=classes)


@classes_blueprint.route("/classes/<id>/edit", methods=["POST"])
def edit_classes(id):
    name = request.form["name"]
    size = request.form["size"]
    time = request.form["time"]
    classes = classes_repository.select(id)
    classes.name = name
    classes.size = size
    classes.time = time
    classes_repository.update(classes)
    return redirect("/classes")


# @classes_blueprint.route("/classes/<id>")
# def show(id):
#     class1 = classes_repository.select(id)
#     return render_template("classes/show.html", classes=classes, members= members)
