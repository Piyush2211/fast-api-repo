# Write a function that takes variable number for argument  and return there sum 
# so basically jabh ham apne functions keh andar dynamic arguments lena chahte hai to perfom a operation in the function on those argument  and return the result than  hum during defination of the function def function_name(*parameter): paas kar sakte hai  

# basically * seh define karenge
   
size_of_list = int(input("Enter the size of the list"))
user_input = []
for x in range(size_of_list):
    user_value = int(input("Enter the value in the list : "))
    user_input.append(user_value)

print(user_input)

def user_value_sum(*sum_operators):
    total_sum =0
    for value in sum_operators:
        total_sum = total_sum + value
    
    return total_sum

total_sum_list = user_value_sum(*user_input)

print("the total sum of the list is : "+str(total_sum_list))
