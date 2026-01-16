# Create a function that accepts  any number of keyword arguments and print them in the format key: value
user_details  ={
    
}
user_details["username"] = input("please enter a username :")
user_details["address"]= input("please enter your address:")
user_details["age"]= input("please enter your age:")

def user_details_string(**user_value):
    for key , value in user_value.items():
        print(f" {key}:{value}")

user_details_string(**user_details)