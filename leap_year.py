# starting_year = 1
# print("Starting from year", starting_year, ", ", end="")
# input_year = int(input("Enter year to print the next 20 leap years: "))
# leap_yr_list = []
#
# if (input_year % 4 == 0) and (input_year % 100 != 0) or (input_year % 400 == 0):
#     for i in range(20):
#         input_year += 4
#         if (input_year % 4 == 0) and (input_year % 100 != 0) or (input_year % 400 == 0):
#             leap_yr_list.append(input_year)
#     print(leap_yr_list)
# else:
#     for x in range(5):
#         for i in range(20):
#             input_year += 4
#             if (input_year % 4 == 0) and (input_year % 100 != 0) or (input_year % 400 == 0):
#                 leap_yr_list.append(input_year)
#         print(leap_yr_list)


starting_year = 1
print("Starting from year", starting_year, ", ", end="")
input_year = int(input("Enter year to print the next 20 leap years: "))
leap_yr_list = []

if input_year / 4 == 0.75:
    input_year += 1
elif input_year / 4 == 0.5:
    input_year += 2
elif input_year / 4 == 0.25:
    input_year += 3

print("input year:", input_year)
for i in range(input_year, input_year + 20):
    input_year += 4
    if (input_year % 4 == 0) and (input_year % 100 != 0) or (input_year % 400 == 0):
        leap_yr_list.append(input_year)
print(leap_yr_list)