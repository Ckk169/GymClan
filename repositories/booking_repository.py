from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.classes_repository as classes_repository


def save(booking):
    sql = "INSERT INTO bookings(member_id, class_id) VALUES (?,?) RETURNING id"
    values = [booking.member.id, booking.classes.id]
    print(booking.member.id)
    results = run_sql(sql, values)
    booking.id = results[0]["id"]
    return booking


def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        # member = member_repository.select(result["member_id"])
        # class1 = classes_repository.select(result["class_id"])

        booking = Booking(result["member"], result["class1"], result["id"])
    return booking


# fix!!!


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row["member_id"])
        classes = classes_repository.select(row["class_id"])
        booking = Booking(classes, member, row["id"])
        bookings.append(booking)
    return bookings


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = ?"
    values = [id]
    run_sql(sql, values)
