# Classify a persons age group: Child (<13), Teenager(13-19),Senior(60+)
user_age = int(input("Enter your age for the verification: \n"))
if 0<user_age<13:
    print("your are a child :"+str(user_age))
elif 13<=user_age<=19:
    print("you are a teen ager :"+str(user_age))
elif 20<=user_age<=59:
    print("You are a adult : "+str(user_age))
elif 0<user_age<60:
    print("your are Senior: "+str(user_age))
elif user_age<0:
    print("age must be postive")
