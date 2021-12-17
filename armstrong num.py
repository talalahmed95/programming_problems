num = input("Enter number: ")
num_list = []
output = 0

for item in num:
    item = int(item)
    item = item * item * item
    num_list.append(item)

num = int(num)

for i in range(len(num_list)):
    output = output + num_list[i]

if num == output:
    print("This is Armstrong/Narcissistic Number")
else:
    print("This is NOT Armstrong/Narcissistic Number")

#print(num_list)
#print(output)