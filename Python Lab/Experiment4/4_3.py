print("Parth Dagar URN:2581361")
students = {"101": {"name": "Rahul", "age": 20, "marks": {"math": 85, "science": 90}},
             "102": {"name": "Priya", "age": 21, "marks": {"math": 78, "science": 88}}}

print("Name:", students["101"]["name"])
print("Math Marks:", students["101"]["marks"]["math"])

for roll_no, details in students.items():
    print("\nRoll No:", roll_no)
    for key, value in details.items():
        print(f"{key}: {value}")

students["101"]["marks"]["english"] = 92
students["103"] = {"name": "Aman", "age": 19, "marks": {"math": 80, "science": 75}}

print("\nUpdated Dictionary:")
print(students)
