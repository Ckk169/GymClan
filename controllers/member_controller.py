from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from models.booking import Booking
from models.classes import Classes

import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/members'
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template(
        "members/index.html", title="GYM Members", all_members=members
    )


@members_blueprint.route("/members/add", methods=["GET"])
def add_member():
    members = member_repository.select_all()
    return render_template("members/add.html", all_members=members)


# CREATE
# POST '/members'
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]

    member = Member(first_name, last_name)
    member_repository.save(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>")
def members_page(id):
    members = member_repository.select(id)
    return render_template(
        "members/member.html", title="GYM Members", members=members
    )

# EDIT
# GET '/members/<id>/edit'
@members_blueprint.route("/members/<id>/edit", methods=["GET"])
def edit_view_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member=member)


@members_blueprint.route("/members/<id>/edit", methods=["POST"])
def edit_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    member = member_repository.select(id)
    member.first_name = first_name
    member.last_name = last_name
    member_repository.update(member)
    return redirect("/members")
