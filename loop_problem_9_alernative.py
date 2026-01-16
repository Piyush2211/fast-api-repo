# check if the elements in the list are unique .if a duplicate is found , exit the loop and print the duplicate
# We have a hash map or dictonary in python check the duplicate in the list 
list_size = int(input("please enter the size of the list "))
user_list = []
checker = {}
for num in range(list_size):
    user_list_value = input("Enter the value in the list :")
    user_list.append(user_list_value)

print(user_list)

for value in user_list :
    if value in checker:
        print("the "+ value + " is duplicate in the list")
        break
    else:
        checker[value]= True