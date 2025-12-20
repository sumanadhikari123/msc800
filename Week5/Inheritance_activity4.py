
# Base Class

class Person:
    """
    Base class representing a person.
    """
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")



# Student inherits Person

class Student(Person):
    """
    Student class inherits from Person.
    """
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")



# Staff inherits Person

class Staff(Person):
    """
    Staff class inherits from Person.
    """
    def __init__(self, person_id, name, staff_id, tax_num):
        super().__init__(person_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display(self):
        super().display()
        print(f"Staff ID: {self.staff_id}")
        print(f"Tax Number: {self.tax_num}")


# General inherits Staff

class General(Staff):
    """
    General staff inherits from Staff.
    """
    def __init__(self, person_id, name, staff_id, tax_num, rate_of_pay):
        super().__init__(person_id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay

    def display(self):
        super().display()
        print(f"Rate of Pay: ${self.rate_of_pay}")



# Academic inherits Staff

class Academic(Staff):
    """
    Academic staff inherits from Staff.
    """
    def __init__(self, person_id, name, staff_id, tax_num, publications):
        super().__init__(person_id, name, staff_id, tax_num)
        self.publications = publications

    def display(self):
        super().display()
        print(f"Publications: {self.publications}")



# Testing the classes

print("\n--- Student ---")
student = Student(1, "Alice", "S101")
student.display()

print("\n--- General Staff ---")
general_staff = General(2, "Bob", "ST201", "TX9988", 30.50)
general_staff.display()

print("\n--- Academic Staff ---")
academic_staff = Academic(3, "Dr. Smith", "ST301", "TX7766", 15)
academic_staff.display()
