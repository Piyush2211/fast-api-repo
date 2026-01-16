# Compute the factorial of a number using while loop
user_number= int(input("Enter a the number whoes factorial you want to find: \n"))
orignal_number = user_number
factorial_value =1 
while user_number != 0:
    factorial_value = factorial_value * user_number
    user_number = user_number - 1

print("the factorial for : \n"+str(orignal_number)+"\nis : \n"+str(factorial_value))