num = input("enter a number: ")
num_list = []
res = []
num = int(num)
for i in range(num):
    res.append(i+1)
    res.append(num * (i+1))

print(res)

print("======================")
for x in res:
    print(num, "x", x, "=", x)