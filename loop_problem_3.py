# Print the multiplication table for the given number upto 10 but skip the fifth iteration
user_input = int(input("Entet the number for which you need the multiplication:\n"))
user_skip = int(input("Enter the number for which you want to skip the iteration:\n"))
for counter in range(1,11):
    
    if counter == user_skip:
        pass
    else:
        print(str(user_input)+"X"+str(counter)+" = "+str(user_input * counter))
 
    