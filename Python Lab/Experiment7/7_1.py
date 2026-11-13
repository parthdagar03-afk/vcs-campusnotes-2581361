print("Parth Dagar URN:2581361")
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

with open("sample.txt", "a") as file:
    file.write("This line is added later.\n")

print("File Content:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

with open("sample.txt", "r") as file:
    line_count = sum(1 for line in file)

print("Number of lines in file:", line_count)
