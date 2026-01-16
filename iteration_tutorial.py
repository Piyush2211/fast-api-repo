user_list = []

for item in range(5):
    user_value = int(input("Enter items in the list: "))
    user_list.append(user_value)

iter_refer = iter(user_list)
for item in range(len(user_list)): 
  print("this is the iter() function reference : "+str(iter_refer)+" this is the value via __next__ ",str(iter_refer.__next__()))# so basicallly hame yaha iseh line koh print karke yeh patah chal jayega keh iter() function keh value hamesha same rahegi vo hamseha iteratable object keh first memory block keh address koh point karega and __next__() iterate karega different values keh upar 
file_handler = open("loop_problem_9.py")

print(str(file_handler is iter(file_handler)))