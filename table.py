multiplier = input("enter multiplier: ")
multiplicand_range = input("enter multiplicand range: ")

product_list = []

multiplier = int(multiplier)
multiplicand_range = int(multiplicand_range)

for i in range(multiplicand_range):
    product_list.append(multiplier * (i+1))

for index, val in enumerate(product_list):
    print(multiplier, "x", index+1, "=", val)