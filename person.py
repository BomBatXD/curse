class Person:
    def __init__(self, personal_name, last_name):
        self._personal_name = personal_name
        self._last_name = last_name

    def full_name(self):
        print(f"The person's full name is {self._personal_name} {self._last_name}")


p = Person("Jhon", "Lock")

p.full_name()