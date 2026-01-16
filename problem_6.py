# Choose  a mode  of transporation based on the distance (e.g <3km: Walk,3-15 km:Bike,15 Km: Car)
user_distance = int(input("Enter the distance you want to cover "))
if user_distance <=3:
    print("You can walk for the distance")
elif 3 < user_distance <=15:
    print("you can use the bike")
elif 15 < user_distance :
    print("You can use the car for this distance ")
