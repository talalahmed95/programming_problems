num = input("Enter number: ")
num_list = []
output = 0
for item in range(int(num)):
    num_list.append(item+1)

for item in range(len(num_list)):
    output += num_list[item]

print("Sum of all numbers till", num, "is", output)