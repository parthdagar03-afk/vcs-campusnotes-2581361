print("Parth Dagar URN:2581361")
READ = 0b100 #4
WRITE = 0b010 #2
EXECUTE = 0b001 #1

permissions = 0b000 #0
print("Iniatial permissions:" , bin(permissions))

permissions = permissions | READ
permissions = permissions | WRITE
print("After adding READ and WRITE permissions:", bin(permissions))

has_execute = permissions & EXECUTE
print("Has EXECUTE permission?:", bool(has_execute))

permissions = permissions | EXECUTE
print("After adding EXECUTE permission:", bin(permissions))

permissions = permissions & ~WRITE
print("After removing WRITE permission:", bin(permissions))