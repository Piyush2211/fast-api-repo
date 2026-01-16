# Calulate the sum of even numbers up to a given Number n 
user_input= int(input("Enter the number for Even sums:\n"))
even_sum_count = 0
for x in range(user_input+1):
  if(x%2==0):
    even_sum_count =  even_sum_count + x
    # print(even_sum_count)

print("the sum of even numbers is : \n"+str(even_sum_count))
