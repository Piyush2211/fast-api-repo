# Reverse a string using a loop
user_string = input("Enter a string you want to reverse:\n")
reverse_string = ""
user_string_size = len(user_string)
while(user_string_size !=0):
    reverse_string= reverse_string + user_string[user_string_size-1]
    print(reverse_string)
    user_string_size -=1

print("The user string is : \n"+user_string+"The reverse string is : \n"+reverse_string)