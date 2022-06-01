from email.errors import MultipartInvariantViolationDefect
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking

import repositories.booking_repository as booking_repository
import repositories.classes_repository as classes_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/bookings'


@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/booking.html", all_bookings=bookings)


@bookings_blueprint.route("/bookings/<id>")
def booking_page(id):
    bookings = booking_repository.select(id)
    # member = member_repository.select_all(id)
    # classes = classes_repository.select_all(id)
    return render_template("bookings/booking.html", all_bookings=bookings)


# @members_blueprint.route("/members/<id>")
# def members_page(id):
#     members = member_repository.select(id)
#     return render_template(
#         "members/member.html", title="GYM Members", members=members
#     )


@bookings_blueprint.route("/bookings/add", methods=["GET"])
def members_booking():
    members = member_repository.select_all()
    classes = classes_repository.select_all()
    return render_template("bookings/add.html", members=members, classes=classes)


@bookings_blueprint.route("/bookings", methods=["POST"])
def show_members_booking():
    member_id = request.form["member_id"]
    classes_id = request.form["classes_id"]
    member = member_repository.select(member_id)
    classes = classes_repository.select(classes_id)
    booking = Booking(classes, member)
    booking_repository.save(booking)
    return redirect("/bookings")
