import matplotlib.pyplot as plt
years = [2018, 2019, 2020, 2021, 2022]
sales_growth = [5, 7, 3, 10, 8]  

plt.figure(figsize=(10, 6)) 
plt.plot(years, sales_growth, marker='o', linestyle='-', color='b')
plt.xlabel('Year')
plt.ylabel('Sales Growth (%)')
plt.title('Annual Sales Growth from 2018 to 2022(Parth Dagar URN:258361)')
plt.grid()
plt.savefig('sales_growth.png')
plt.show()
