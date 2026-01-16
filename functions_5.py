# Write a function that greets a user. if no name is provided , it should greet with default name 
user_name = input("Please Enter your name: ")

def greet_function(user_name = "Sir/Madam"):
  print(f"Welcome {user_name} to coding in python")

greet_function(user_name)
greet_function()  
