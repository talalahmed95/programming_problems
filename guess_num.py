# num_to_guess = str(3)
# num_to_guess_len = len(num_to_guess)
# print("The number to guess is", num_to_guess_len, "digits")
# matched = False
# tries = 0
# guess_list = []
# while matched == False:
#     num = int(input("Enter a number: "))
#     num_to_guess = int(num_to_guess)
#     guess_list.append(num)
#     for i, val in enumerate(guess_list):
#         # j = i + 1
#         for j in range(i + 1, len(guess_list)):
#         # for j, val2 in enumerate(guess_list):
#             # j = i + 1
#             # print("index of j:", j, ":: value of mj:", guess_list[j])
#             # print("val:", val, ":: [j]:", guess_list[j])
#             if val == guess_list[j]:
#                 # print("i:", i, ":: val i:", val, ":::: j:", j, ":: val j:", guess_list[j])
#                 # print("xxxxxxxxx INCREMENT xxxxxxxxxx")
#                 tries += 1
#
#     if num > num_to_guess:
#         print("guessed number is LARGER than the number to be guessed")
#     elif num < num_to_guess:
#         print("guessed number is SMALLER than the number to be guessed")
#     else:
#         # print("Congrats! your guess is correct. It took you", tries, "tries")
#         print("Number of duplicates:", tries)
#         matched = True

# num_to_guess = str(3)
# num_to_guess_len = len(num_to_guess)
# print("The number to guess is", num_to_guess_len, "digits")
# matched = False
# tries = 0
# guess_list = []

# while matched == False:
#     num = int(input("Enter a number: "))
#     num_to_guess = int(num_to_guess)
#     guess_list.append(num)
#     for i in range(len(guess_list)):
#         for j in range(i+1, len(guess_list)):
#             tries += 1
#
#     if num > num_to_guess:
#         print("guessed number is LARGER than the number to be guessed")
#     elif num < num_to_guess:
#         print("guessed number is SMALLER than the number to be guessed")
#     else:
#         # print("Congrats! your guess is correct. It took you", tries, "tries")
#         print("Number of duplicates:", tries)
#         matched = True


guess_list = ['a', 'a', 'b', 'a', 'c', 'z', 'c', 'n', 'k', 'a']
res = []
res2 = []
tries = 0
for i in range(len(guess_list)):
    for j in range(i+1, len(guess_list)):
        # if guess_list[i] == guess_list[j]:
        #     print(guess_list[i], guess_list[j])
        #     tries += 1

        if guess_list[i] == guess_list[j]:
            res.append(guess_list[i])
            res2.append(guess_list[j])
            if guess_list[j] in res:
                print(guess_list[i], guess_list[j])
                tries += 1

print("Number of dup:", tries)
print(res)
print(res2)
