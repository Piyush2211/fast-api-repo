# Create a function that return  both circumference and area of cirle given its radius


user_input =int(input("Enter the radius of the cirle for area and circumference: "))
def area_circum_of_circle(radius):
    circle_measure = {}

    circle_measure["area"]= 3.14*(radius**2)
    circle_measure["circumfrence"]=2*3.14*radius
    return circle_measure

circle_value = area_circum_of_circle(user_input)

print("the area of circle : \n" + str(circle_value.get("area")) + "\n the circumfrence of the circle is : \n "+ str(circle_value.get("circumfrence")) )

