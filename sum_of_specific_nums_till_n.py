# only calculate sum if input is divisible by 3 or 5
num = input("Enter number: ")
num_list = []
output = 0
for item in range(int(num)):
    num_list.append(item+1)

num = int(num)
for item in range(len(num_list)):
    if num % 3 == 0 or num % 5 == 0:
        output += num_list[item]

print("Sum of all numbers till", num, "is", output)