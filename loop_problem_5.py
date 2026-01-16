# Given a string find the first non repeated character
user_input = input("Enter a string favourable which repeat some character in the string ")
for x in range(len(user_input)):
    if user_input.count(user_input[x])==1:
        print(user_input[x]+"is at:"+str(x))
        break

