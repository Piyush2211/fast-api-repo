# Check  if a password is Weak ,Medium or Strong Criteria: <6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)
# user_password = input("Enter a  password ") 
import re
user_password = input("Enter the password ")
if (
    re.search(r'[a-z]', user_password) and   # lowercase
    re.search(r'[A-Z]', user_password) and   # uppercase
    re.search(r'[0-9]', user_password) and   # digit
    re.search(r'[@#$%!]', user_password) and # special character
    len(user_password) >= 12
):
    print("Password is strong")
elif  re.search(r'[A-Z]',user_password) and len(user_password)>10:
    print("Password is good")
elif len(user_password)<10:
    print("Password is weak ")
else:
    print("password is very weak we suggest to change")