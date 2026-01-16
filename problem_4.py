# Determine if a fruit is ripe,overripe, unripe  based on the its color .(eg.Banaa:Green-unripe,yellow-ripe,Brown-overripe)
user_banana_color = input("Enter the color of banana:\n").lower()
if user_banana_color == "yellow":
    print("The banana is ripped")
elif user_banana_color == "green":
    print("The banana is unripped")
elif user_banana_color == "brown":
    print("The banana is over ripped")
else:
    print("please enter a valid color")
