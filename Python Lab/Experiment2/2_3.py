print("Parth Dagar URN:2581361")
n = int(input("Enter a number: "))

if n <=1 :
    print("Not a Prime")
else :
    for i in range(2,n):
        if n % i == 0:
            print("Not a Prime")
            break
    else:
        print("Prime")
