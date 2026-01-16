# Write a generator function that yields even numbers up to a specified limit 

def even_generator (limit): # so basically generator function basically isliye design kiya jaata hai taki hum ek iterator tool keh andar uska use karke ek specific value ko produce kar sake
    for gen_iter in range(2,limit+1):
        if gen_iter%2 ==0 : 
            yield gen_iter  # so basically yeild keyword bhi return wale kaam hi karta hai par yeh  function koh end nahi karta as return keh tarah  yeh function  basically allotted memory relase nahi karta hai jiseh  generation create ho jata hai   

# def even_non_genrator (limit):
#     for gen_iter in range(2,limit+1):
#         if gen_iter%2 ==0:
#             return gen_iter

user_input = int(input("Enter the number for which you need the even numbers till a range:  "))

for i in even_generator(user_input):
    print(i)

# for i in even_non_genrator(user_input):
#     print(i)
