from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member


def save(member):
    sql = "INSERT INTO members( first_name,last_name )VALUES( ?,? ) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row["first_name"], row["last_name"], row["id"])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result["first_name"], result["last_name"], result["id"])
    return member


def delete(id):
    sql = "DELETE FROM members WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def update(member):
    sql = "UPDATE members SET(first_name,last_name) = (?,?) WHERE id = ?"
    values = [member.first_name, member.last_name, member.id]
    run_sql(sql, values)
