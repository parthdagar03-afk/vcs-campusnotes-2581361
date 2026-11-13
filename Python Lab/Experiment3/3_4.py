print("Parth Dagar URN:2581361")
my_tuple = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("Original Tuple:", my_tuple)

print("\n--- Accessing Elements ---")
print("Element at index 1:", my_tuple[1])
print("Last element:", my_tuple[-1])
print("Sliced tuple (1 to 3):", my_tuple[1:4])

print("\n--- Updating Tuple ---")
new_items = ("Pineapple", "Cherry")

updated_tuple = my_tuple + new_items
print("After Concatenation:", updated_tuple)

repeated_tuple = my_tuple * 2
print("After Repetition:", repeated_tuple)

print("\n--- Deleting Tuple ---")
temp_tuple = ("A", "B", "C")
print("Temporary Tuple:", temp_tuple)
del temp_tuple
print("Temporary Tuple deleted successfully!")

print("\n--- Iterating Over Tuple ---")
for item in my_tuple:
    print(item)

search_item = "Mango"
if search_item in my_tuple:
    print(search_item, "is found in the tuple.")
else:
    print(search_item, "is not found in the tuple.")
