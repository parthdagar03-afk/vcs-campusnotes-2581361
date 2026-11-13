print("Parth Dagar URN:2581361")
with open("Source.txt", "r") as source:
    
    with open("Sample.txt", "a") as target:
        
        for line in source:
            target.write(line)

print("Content copied successfully!")