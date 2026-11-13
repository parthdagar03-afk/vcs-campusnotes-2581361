print("Parth Dagar URN:258361")
import pandas as pd
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Marks': [85, 42, 38, 90, 55]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
passed_students = df[df['Marks'] >= 40]
print("\nStudents who passed (Marks >= 40):")
print(passed_students)
