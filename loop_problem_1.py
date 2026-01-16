# Given a list of numbers , count how many are positive number = [1,-2,3,-4,-5.-6,-7,6,9,10]
numbers = []
size_of_list = int(input("Please enter the size of list in postive integer: \n"))
for num in range(size_of_list):
    value = int(input("Enter a postive or negative  numbers in the list:  \n"))
    numbers.append(value)

print(numbers)
postive_counter = 0
negative_counter = 0
for nums in numbers:
    if nums > 0:
        postive_counter +=1
    elif nums <0:
        negative_counter +=1

print("no of digits postive in the list are: \n"+str(postive_counter))
print("no of digits negative in the list are : \n"+str(negative_counter)) 
