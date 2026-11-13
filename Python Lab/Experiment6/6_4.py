print("Parth Dagar URN:2581361")
def calculate_average(students_dict):
    averages = {}
    
    for student, marks in students_dict.items():
        avg = sum(marks) / len(marks)
        averages[student] = avg
    
    return averages

students = {
    "Aarti": [78, 85, 90],
    "Rahul": [60, 70, 65],
    "Sneha": [88, 92, 95]
}

result = calculate_average(students)
print(result)
