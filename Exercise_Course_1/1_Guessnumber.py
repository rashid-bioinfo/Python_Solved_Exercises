# Write a program to guess a number

hidden_number = 20

guess_number = 0

while (guess_number != hidden_number):
    guess_number = int(input("Guess a number: "))
    if (guess_number < hidden_number):
        print("Please try a bigger number")
    elif (guess_number > hidden_number):
        print("Please try a smaller number")
else:
    print(f" Congratulation! numbers are MATCHED: {guess_number} = {hidden_number}")

