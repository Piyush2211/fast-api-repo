# Create a car class with attributes like brand and model. Then create an instance of this class    
# add a method to the car class that display full name of the car(brand and model)
# Create an Electric class that inherites from the car class and has additional attributes battery_size
# Modify the car class to encapsulate the brand attribute, making it private and provide a getter method on it
# Demonstrate the use of isinstance to check if tesla_car is a instance  of Car and Electric_car
# Create two classes Battery and Engine, and let the Electric_car class inherit from both ,demonstrating  multiple inheritence
class Car:
    brand = None
    __model = None
    __engine_size = None
    def __init__ (self, brand , model):#__init__ is basicallya constructor which will call itself as we create the object of the class  in other words yeh constructor hai  joh object baneh par apne aap call hoga 
        self.brand = brand # class keh andar jabh bhi hum koi function define karenge toh uske andar atleast hame ek parameter rakhna hi padega kyuki python meh jabh hum kiseh class keh object seh uske method koh call karte hai toh vo object as a argument apne aap koh paas karta hai function joh yaha par self meh use hoga jiseh ek link create hota hai  class keh andar keh variables aur class keh bahar idhar self bhi wahi hai 
    
        self.__model = model # so python meh variable koh private karne keh liye uske naam keh aage 2 underscore use hote hai basically like __variable_name iseh hum iseh variable koh class keh bahar nahi use kar sakte
        # basically python meh agar public karna ho variable yah method koh toh hum koi underscore nahi lagate basic naam use karte hai jese variable_name
        # agar variable yah function koh hame protected karna ho toh hum ek underscore use kare hai jese _variable_name protected karne seh hamre variable sub class keh andar access ho sakte hai par bahar nahi sub class basically vo class hai joh  variable jah define hai useh class koh access karegi  
                
    

    def car_model(self):
        return f"{self.brand} {self.__model} "
    
    def get_model(self):# basically yeh ek getter function hai joh private variables of a class keh values return karne keh liye banaya jaata hai
        return self.__model + "!"
    
    def set_engine_size(self,engine_size):#Basically yeh ek setter function hai joh private variables of a class keh values koh set karne keh liye use hota hai 
        self. __engine_size = engine_size
    
    def get_engine_size(self):
        return self.__engine_size
         
    def class_functiion_without_self(not_self):    
         brand  = 24
         print(f"{not_self.brand}")

class Electric_car(Car) :# so basically python meh agar hame kise class koh inherit karna hota hai toh hum useh class koh () keh andar pass karte hai
    def __init__(self,brand , model , battery_size):
        super().__init__(brand,model)# basically yaha par humne super() keyword use kiya hai toh parent class keh variables , __init__() constructor , same name function keh andar prop pass karne keh liye , value store karane keh liye store hota hai
        
        self.battery_size = battery_size

    


my_car = Car("Toyota","Hilux")
print(my_car.brand)
# print(my_car.__model)  # So basically hamne model koh private kardiya tha class meh __use karke toh ham useh class keh bahar abh eseh class nahi kar sakte hame atribute_error milega  
print(my_car.get_model())# to basically to overcome this hum get_model use karenge  joh hamare private variable keh values return karega class seh 
car_full_name = my_car.car_model()
print(car_full_name)
my_car.set_engine_size("1400cc")
print(my_car.get_engine_size())

my_car.class_functiion_without_self() # basically jabh hum eseh call karenge apne class_functiion_without_self() koh  toh iseh function meh python apne aap my_car koh pass karega  par humne defination keh time par koi parameter nahi paas kiya hua toh error aayega  basically eseh hora hai class_function_without_self(my_car) but koi  bhi parameter nah hone keh karan error aayega

tesla_car = Electric_car("Tesla","s500","500w")
print(tesla_car.brand)
print(tesla_car.car_model())
print(isinstance(tesla_car,Car))
print(isinstance(tesla_car,Electric_car))

class Physics():
    def test_physics(self):
        print("This the physics class")

class Math():
    def test_math(self):
        print("this is the math class")

class Favouraite_subject(Physics,Math):
    pass

my_fav_subject = Favouraite_subject()

print(my_fav_subject.test_math(),my_fav_subject.test_physics())# we are getting None None in end because we are printing the values returned by the  function and functions are returning None , None 