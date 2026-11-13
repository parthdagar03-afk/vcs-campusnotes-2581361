print("Parth Dagar URN:258361")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # marks should be a list

    def calculate_total(self):
        return sum(self.marks)

name = input("Enter student name: ")
marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

student = Student(name, marks)

total = student.calculate_total()

print("Student Name:", student.name)
print("Total Marks:", total)