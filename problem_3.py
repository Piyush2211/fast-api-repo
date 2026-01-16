# Assign a letter grade based on a students score: A(90-100),B(80-90),C(70-79),D(60-69),F(below 60)
user_math_marks = int(input("Enter the math marks : \n"))
user_science_marks = int(input("Enter the science marks : \n"))
user_English_marks = int(input("Enter the English marks :\n"))
if user_math_marks >100 or user_science_marks>100 or user_English_marks >100:
    print("please  verify that you have entered marks in range of 100\n")
    exit()
agregate_marks = ((user_science_marks +user_math_marks+user_English_marks)/300)*100
print(agregate_marks)
if (90 < agregate_marks <=100):
    print("you have A grade")
elif(80< agregate_marks <=90 ):
    print("you have B grade")
elif(70 < agregate_marks<=80):
    print("you have C grade")
elif(60<agregate_marks<=70):
    print("you have D grade")
else:
    print("you have F grade")
