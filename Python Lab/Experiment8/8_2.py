print("Parth Dagar URN:258361")

class Student:
    def __init__(self, name=None, age=None, grade=None):
        if name is None and age is None and grade is None:
            self.name = "Default Name"
            self.age = 0
            self.grade = "Not Assigned"
        else:
            self.name = name
            self.age = age
            self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


student1 = Student()
student1.display()

print()

student2 = Student("Parth", 20, "A")
student2.display()