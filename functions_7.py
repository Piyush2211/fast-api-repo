# Write a function which return variable as a argument and return their sum 
size_of_list = int(input("Enter the size of the list you want for the list :"))
user_input = []
for i in range(size_of_list):
    user_value = int(input("Enter the value in the list :"))
    user_input.append(user_value)

def sum_of_list(*args):# with using *parameter_name hum  mutliple arguments pass kar rahe hai apne functions meh . basically *parameter_name seh python ek tuple meh store karega arguments koh joh  firh hamara function use karega inpe operations perform karne keh liye 
    sum =0
    for value in args:
        sum = sum + value 

    return sum 


print("the sum of the value is : "+ str(sum_of_list(*user_input)))# so basically jabh bhi hum ek argument pass karenge joh keh iterable ho toh hame useh functions meh pass karne keh liye dstruct karna hi padega in order to iterate its value