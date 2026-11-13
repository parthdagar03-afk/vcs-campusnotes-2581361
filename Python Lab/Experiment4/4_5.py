print("Parth Dagar URN:2581361")
text = input("Enter a line: ")

upper = lower = digits = alphabets = 0

for ch in text:
    if ch.isupper():
        upper += 1
    if ch.islower():
        lower += 1
    if ch.isdigit():
        digits += 1
    if ch.isalpha():
        alphabets += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Alphabets:", alphabets)
