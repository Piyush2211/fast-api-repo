# Keep asking the user for a number until they enter a number between 1-10
user_value_not_in_range = True

while (user_value_not_in_range):
    user_value = int(input("Guess a number"))
    if 1<=user_value<=10:
        print("You have guessed the correct no : "+str(user_value))
        user_value_not_in_range = False
    else:
        print("You have guessed wrong")
