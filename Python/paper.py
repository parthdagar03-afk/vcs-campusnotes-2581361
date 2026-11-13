with open("Sample.txt", "r") as f:
    content = f.read()
search = content.find("learning")
if search == -1:
    print("Not found")
else:
    print("Found")