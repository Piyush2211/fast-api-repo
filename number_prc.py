import math
import random 
from decimal import Decimal
from fractions import Fraction

# python integer float koh toh as a number carry karta hi hai sath sath meh complex no (1+2j), fractions(2/7), decimal koh bhi carry karta hai apne sath sath  basically hum inpe operations perform kar sakte hai 
user_number_1 = int(input("Enter the no you want to use \n")) 
user_number_2 = int(input("Enter the 2nd no you want to use\n"))
user_number_3 = int(input("Enter the the third number \n"))

number_sum = user_number_1 + user_number_2
number_mutiple = user_number_1 * user_number_2
number_divide = user_number_1 / user_number_2
number_power = user_number_1 ** user_number_2
number_modulus = user_number_1 % user_number_2
print("the answers of the numbers are"+" "+str(user_number_1) + " " +str(user_number_2) + " " +str(number_sum)+ " " +str(number_mutiple)+ " " +str(number_divide)+ " " +str(number_power)+ " " +str(number_modulus))
print(user_number_1 + user_number_2 == user_number_3)# this is not a good practise to make expressions like this we should  pranthises for operations  precidence in order to work correctly() btw the python basically converts this expression in  (user_number_1 + user+_number_2) == user_number_3 

decimal_number_1 = Decimal(str(input("enter a number")))
print(decimal_number_1+Decimal('0.1'))
myfra = Fraction(2,7)
print(myfra)
# when we use mutliple variable together such as x,y,z than we will get as result  (x_value,y_value,z_value)
# python will provide us a proper precission to almorst infite we will get large numbers
print(2**100)
#python will provide us large decimal values in decimal too we have many functions to deal with it such as 
string_1 = "this is the string"
print(repr(string_1))# repr will provide us the offical reprentation of the string or litreal
print(repr(22/7))
print(str(string_1))# string will provide us the value which is represented to the user or customer
print(str(22/7)) #
result_no = 1==2<3
print(result_no)
print(math.floor(12.56),math.floor(-4.5))
print((2+3j) +(4+5j))
print(oct(56))
print(hex(112))
print(bin(223))
print(int('131',7))
print(random.random())
print(random.randint(1,100))
array_1 = ['lemon','mango','banana']

print(random.choice(array_1))


