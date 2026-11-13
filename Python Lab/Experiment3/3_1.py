print("Parth Dagar URN:2581361")
n = [10,45,67,18,77]
print("Original list:",n)

print("Elment at index 3:",n[3])

n[1] = 47
print("Updated list:",n)

del n[2]
print("List after deleting element:",n)

n.sort()
print("Sorted list:",n)

search_element = int(input("Enter element to search: "))

if search_element in n:
    print(search_element, "found at index", n.index(search_element))
else:
    print(search_element, "not found in the list")
