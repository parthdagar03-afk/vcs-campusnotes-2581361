print("Parth Dagar URN:2581361")
def get_unique_words(filename):
    unique_words = set()
    
    with open(filename, "r") as file:
        for line in file:
            words = line.strip().replace('.', '').replace(',', '').split()
            for word in words:
                unique_words.add(word.lower())  
    
    return sorted(unique_words)

def count_lines_starting_with_f(filename):
    count = 0
    
    with open(filename, "r") as file:
        for line in file:
            if line.strip().startswith('F'):
                count += 1
    
    return count

file_name = "sample.txt"

words = get_unique_words(file_name)
print("Unique words (alphabetical order):")
print(words)

f_count = count_lines_starting_with_f(file_name)
print("\nNumber of lines starting with 'F':", f_count)