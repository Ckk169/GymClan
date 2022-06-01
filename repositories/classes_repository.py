from db.run_sql import run_sql
from models.classes import Classes
from models.member import Member


def save(gym_class):
    sql = "INSERT INTO classes(name,size,time) VALUES(?,?,?)RETURNING id"
    values = [gym_class.name, gym_class.size, gym_class.time]
    results = run_sql(sql, values)
    gym_class.id = results[0]["id"]
    return gym_class


def select_all():
    classes = []

    sql = "SELECT * FROM classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Classes(row["name"], row["size"], row["time"], row["id"])
        classes.append(gym_class)
    return classes


def select(id):
    gym_class = None
    sql = "SELECT * FROM classes WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Classes(
            result["name"], result["size"], result["time"], result["id"]
        )
    return gym_class


def delete_all():
    sql = "SELECT from classes"
    run_sql(sql)


def update(gym_class):
    sql = "UPDATE classes set(name,size,time = (?,?.?) WHERE id = ?"
    values = [gym_class.name, gym_class.size, gym_class.time]
    run_sql(sql, values)


def member(classes):
    members = []
    sql = "SELECT distinct members.* FROM members INNER JOIN bookings ON members.id = bookings.member_id WHERE bookings.class_id = ?"
    values = [classes.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row["first_name"], row["last_name"], row["id"])
        members.append(member)

    return members
