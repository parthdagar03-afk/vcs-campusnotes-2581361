print("Parth Dagar URN: 2581361")
#Q1
print("Enter your purchased amount: ")
c1=int(input("Customer 1:"))
c2=int(input("Customer 2:"))
c3=int(input("Customer 3:"))
c4=int(input("Customer 4:"))
c5=int(input("Customer 5:"))

c_list=[c1,c2,c3,c4,c5]
def average(c_list):
    sum=0
    for i in c_list:
        sum = sum + i
    avg=sum/5
    return avg
print("Average purchase amount:", average(c_list))
print("-------------------------------------------------------------------------------")
#Q3
class Product:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")

product1 = Product("Laptop", 1200)
product2 = Product("Smartphone", 800)

print("Product 1 Details:")
product1.display()
print("\nProduct 2 Details:")
product2.display()
