# Create  a recursive function to calculate the factorial of a  number

user_value = int(input("Enter a number whose factorial you want to find :"))
def factorial_of_number(number):
    if number == 1:
        return 1 
    else :
        return number * factorial_of_number(number-1)
    
print("the factorial of the number is: "+str(factorial_of_number(user_value)) )