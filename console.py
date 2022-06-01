import pdb

from models.booking import Booking
from models.classes import Classes
from models.member import Member

import repositories.booking_repository as booking_repository
import repositories.classes_repository as classes_repository
import repositories.member_repository as member_repository

member1 = Member("Nicky", "Jone")
member1 = member_repository.save(member1)

member2 = Member("Ally", "Sit")
member2 = member_repository.save(member2)

member3 = Member("Bobby", "Kerr")
member3 = member_repository.save(member3)


class1 = Classes("HITT", 5, "14:00")
class1 = classes_repository.save(class1)

class2 = Classes("Powerlift", 10, "8AM")
class2 = classes_repository.save(class2)

class3 = Classes("Cardio", 15, "10pm")
class3 = classes_repository.save(class3)


booking1 = Booking(member1, class1)
booking_repository.save(booking1)

booking2 = Booking(member2, class2)
booking_repository.save(booking2)

booking3 = Booking(member3, class3)
booking_repository.save(booking3)


pdb.set_trace()
