# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 18
#person class
class Person:
    def __init__(self, age):
        self.age = age
#decide if a person can enter
def enter_night_club(person):
    if older_than_18_year_old(person.age):
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denied.")
#check if the person is older than 28
def older_than_18_year_old(age):
    if age > LEGAL_DRINKING_AGE:
        return True
    else:
        return False


person = Person(17.9)
enter_night_club(person)
