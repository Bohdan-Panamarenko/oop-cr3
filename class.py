import copy
import re


class Organization:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError
        self.__name = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        if not isinstance(value, str) or not re.match("^\\+?\\d{3,14}$", value):
            raise ValueError
        self.__phone = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError
        self.__address = value

    def __str__(self):
        return f"{self.name}: {self.address}, {self.phone}"


class Department(Organization):
    def __init__(self, name, phone, address, speciality, bachelors = 0, specialists = 0, masters = 0):
        super().__init__(name, phone, address)
        self.speciality = speciality
        self.bachelors = bachelors
        self.specialists = specialists
        self.masters = masters

    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, value: str):
        if not isinstance(value, str):
            raise ValueError
        self.__speciality = value

    @property
    def bachelors(self):
        return self.__bachelors

    @bachelors.setter
    def bachelors(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError
        self.__bachelors = value

    @property
    def specialists(self):
        return self.__specialists

    @specialists.setter
    def specialists(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError
        self.__specialists = value

    @property
    def masters(self):
        return self.__masters

    @masters.setter
    def masters(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError
        self.__masters = value

    def all_people(self):
        return self.bachelors + self.specialists + self.masters

    def all_students(self):
        return self.bachelors + self.masters

    def __eq__(self, other):
        if not isinstance(other, Department):
            raise ValueError
        return self.all_people() == other.all_people()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Department):
            raise ValueError
        return self.all_people() > other.all_people()

    def __lt__(self, other):
        if not isinstance(other, Department):
            raise ValueError
        return self.all_people() < other.all_people()

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __str__(self):
        return super().__str__() + f"\nSpeciality: {self.speciality}\nBachelors: {self.bachelors}, specialists: {self.specialists}, masters: {self.masters}"


class Faculty:
    def __init__(self):
        self.__departments = list()

    def __add__(self, other):
        if not isinstance(other, Department):
            raise ValueError
        self.__departments.append(other)

    def __iter__(self):
        return FacultyIterator(self.__departments)

    def all_students(self):
        x = (d.all_students() for d in self.__departments)
        return sum(x)


class FacultyIterator:
    def __init__(self, departments):
        if not isinstance(departments, list):
            raise ValueError
        self.__departments = departments
        self.__counter = 0
        self.__limit = len(departments)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__limit:
            dep = copy.copy(self.__departments[self.__counter])
            self.__counter += 1
            return dep
        else:
            raise StopIteration


d1 = Department("APEPS", "099774135", "some building 2", "Programming", 20, 5, 10)
d2 = Department("IPSA", "099774135", "another building 3", "MATH", 20, 5, 10)

f = Faculty()

f + d1
f + d2

print(f.all_students())
print(d1 == d2)
print("----------")

for d in f:
    print(d)
    print("----------")

