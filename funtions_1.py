# write a function to calculate the square of a number    
user_number = int(input("Enter the number for which you want to find the square: "))

def square_no(square_number):
    return square_number**2

square_number = square_no(user_number)
print("the square of the no  "+str(user_number)+" : = "+str
      (square_number))