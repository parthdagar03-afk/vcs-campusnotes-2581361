print("Parth Dagar URN:2581361")
text = input("Enter a sentence: ")

words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Count:")
for key, value in word_count.items():
    print(key, ":", value)
print("Total words:", len(words))
