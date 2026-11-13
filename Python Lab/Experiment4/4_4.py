print("Parth Dagar URN:2581361")
text = "Hello World"

print("Original String:", text)
print("Slice (0:5):", text[0:5])
print("Slice (6:):", text[6:])
print("Reverse String:", text[::-1])

print("Replication (3 times):", text * 3)

new_text = text + " Programming"
print("Concatenation:", new_text)

replaced_text = text.replace("Python", "World")
print("Replacement:", replaced_text)
