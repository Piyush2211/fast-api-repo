# Recommaned a type of pet food based on the pets species and age (e.g. Dog:<2 Years puppy food , Cat:5 years - Senior cat food  )
user_pet_species = input("Please provide the species of your pet:  \n").lower()
user_pet_age = int(input("please enter the age of your pet: \n"))
print(user_pet_species,user_pet_age)
if user_pet_species == "dog":
    if user_pet_age <2 :
        print("Please buy the puppy food")
    else:
        print("you can buy the normal food for the pet")
elif user_pet_species =="cat":
    if user_pet_age >=5:
        print("please buy the senior cat food ")
    else:
        print("please buy the normal cat food ")
else:
    print("We are in progress of having pet food for species other than cat and dog")