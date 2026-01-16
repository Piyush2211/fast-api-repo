# Check if all elements in a list are unqiue.if a duplicate is found, exit the loop and print the duplicate 
list_size = int(input("Please enter the size of the list\n"))
user_list = []
duplicate_found = False
for user_entry in range(list_size):
    user_entry_value = input("Enter the elment in the list: ").strip()
    user_list.append(user_entry_value)
print(user_list)

for i in range(list_size):
    for j in range(i+1,list_size):
       if  user_list[i]==user_list[j]:
           print(user_list[i]+" is duplicate in the list and comes at index : "+str(i))
           duplicate_found = True
           break
    if duplicate_found :
        break

if not duplicate_found:
    print("There is no duplicate in the list ")





        
