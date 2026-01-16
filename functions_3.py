# Write a function which multiply two numbers , but can also accept and multiply strings
 
def multiplication_handler(string_1:str , string_2:int):
    return string_1 * string_2

def multiplication_handler(number_1:int,number_2:int):
    return number_1 * number_2

print(multiplication_handler("piyush",5))
print(multiplication_handler(5,5))