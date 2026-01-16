# Check if a number is prime
user_input = int(input("enter a number: "))
is_prime = True

for num in range(2,user_input):
    if user_input%num ==0:
        is_prime = False
        break

print("the "+str(user_input)+" is  prime : \n" + str(is_prime)  )
