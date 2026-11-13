print("Parth Dagar URN:2581361")
string = input("Enter a string: ")

cleaned_string = string.replace(" ", "").lower()

if len(cleaned_string) == len(set(cleaned_string)):
    print("The given string is a Heterogram.")
else:
    print("The given string is NOT a Heterogram.")
