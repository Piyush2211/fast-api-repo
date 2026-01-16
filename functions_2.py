# Create a function that takes two numbers as parameters and  returns their sum

user_number_1 = int(input("Enter   first number whose sum you want to find : "))
user_number_2 = int(input("Enter the second number which you want to sum: "))

def sum_of_two_numbers(number_1,number_2):
    return number_1 + number_2

result_of_sum = sum_of_two_numbers(user_number_1,user_number_2)

print("The sum of the numbers is : \n"+str(result_of_sum))