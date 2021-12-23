num = int(input("enter number to check if prime: "))
num_range = int(input("enter range: "))
output = []
try:
    for i in range(num_range):
        if num / (i+1) == 1 and num != 1:
            output.append(1)
        elif num / (i+1) != 1 and num != 1:
            output.append(2)
        elif num == 1:
            output.append(3)
        else:
            output.append(4)
    if 1 in output:
        print("Prime Number")
    elif 2 in output:
        print("Composite Number")
    elif 3 in output:
        print("One is neither prime nor composite")
    elif 4 in output:
        print("neither prime nor composite")

except:
    print("Error Occurred")
