open_file = open("CupcakeInvoices.csv")

for line in open_file:
    print(line)

for line in open_file:
  list = line.split(',')
  print(list[2])

for line in open_file:
  list = line.split(',')
  total = float(list[3]) * float(list[4])
  print(total)

sum = 0
for line in open_file:
  list = line.split(',')
  total = float(list[3]) * float(list[4])
  sum = sum + total

print(sum)

open_file.close()

import matplotlib.pyplot as plt 

x = ["Chocolate", "Vanilla", "Strawberry"]

y = [267.10, 388.6, 164.69]

plt.xlabel('Type of Cupcake')

plt.ylabel('Income')

plt.show() 