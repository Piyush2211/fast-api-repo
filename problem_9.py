# Determine if a year  is a leap year(Leap years are divisible by 4 ,but not by 100 unless it is divisible by 400)
user_birth_year = int(input("Enter the year you were born:\n"))
is_leap_year = bool(user_birth_year%4 ==0 and (user_birth_year%100 !=0 or user_birth_year%400 ==0))
if is_leap_year:
    print("Your birth year is a leap year ")
else :
    print("Your birth year is not a leap year ")