num_to_guess = str(69)
num_to_guess_len = len(num_to_guess)
print("The number to guess is", num_to_guess_len, "digits")
matched = False
tries = 0
guess_list = []
while matched == False:
    num = int(input("Enter a number: "))
    num_to_guess = int(num_to_guess)
    guess_list.append(num)
    print(guess_list)
    for i, val in enumerate(guess_list):
        # j = i + 1
        for j in range(i + 1, len(guess_list)):
            # j = i + 1
            # print("index of j:", j, ":: value of j:", guess_list[j])
            if val == guess_list[j]:
                # print("i:", i, ":: val i:", val, ":::: j:", j, ":: val j:", guess_list[j])
                print("** matched")
                tries += 1

    if num > num_to_guess:
        print("guessed number is LARGER than the number to be guessed")
    elif num < num_to_guess:
        print("guessed number is SMALLER than the number to be guessed")
    else:
        print("Congrats! your guess is correct. It took you", tries, "tries")
        matched = True