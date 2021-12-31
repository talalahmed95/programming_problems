num_to_guess = str(51)
num_to_guess_len = len(num_to_guess)
print("The number to guess is", num_to_guess_len, "digits")
matched = False
tries = 0
guess_list = []
guess_list_without_duplicates = []

while matched == False:
    num = int(input("Enter a number: "))
    num_to_guess = int(num_to_guess)
    guess_list.append(num)
    for i, val in enumerate(guess_list):
        if val not in guess_list_without_duplicates:
            guess_list_without_duplicates.append(val)
            tries += 1
    if num > num_to_guess:
        print("guessed number is LARGER than the number to be guessed")
    elif num < num_to_guess:
        print("guessed number is SMALLER than the number to be guessed")
    else:
        print("Congrats! your guess is correct. It took you", tries, "tries")
        matched = True