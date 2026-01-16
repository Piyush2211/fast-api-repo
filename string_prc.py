name = "piyush sharma"
print(name)
print(name[1])# We can perform same function as list like slicing in strings too
print(name[0:6])# basically slicing me first index use ho skata hai par last index nahi use hota hai 
numlist = "1,2,3,4,5,6,7,8,9"
print(numlist[0:9:2])# in slicing pehla index seh start hoga firh second jaha tak jaana hai vo hoga and last meh jump ayega 

print(numlist[-2:])#negative slicing meh joh abse end wala index hoga e.g -9 hai numlist meh toh string waha seh shuru hoke -1 tak jayegi -1 is the last index or the end index in the negative slicing of string or the list

print( name.lower())# yeh string koh lower case meh convert karega
print(name.upper())# yeh string koh upper case meh convert karega
name_with_space = " Piyush Sharma "
print(name_with_space.strip())# yeh string keh starting aur end seh white spaces remove karega 
print(name.replace("piyush","vasu"))#  yeh function ek string meh seh substring dhundega aur usko replace kardega useh substring seh joh second argument meh paas kare hogi 
print(numlist.split(","))# split function basically ek specific argument leta hai variable keh sath firh jaha jaha vo argument dikhta hai usko string meh waha tak ek substring koh list meh add karta rehta hai and ek array of substring create kardeta hai
print(numlist.find('2,3,4'))# find function basically starting index return kardeta hai jaha seh iske andar paas kari huyi substring paas kari hoti hai  
print(name.find("Sharma"))# find function case senstive hota hai and agar isko substring nahi milti hai toh yeh -1 return kardeta hai 
series_string = " one two two three three three four four four four "
print(series_string.count("three"))# so basically  count function no of substring kitne baar aaye hai batah hai ek string keh andar joh usme paas kari jaati hai 
user_name = input("Enter your name ")
string_template = "Hi {} welcome to the habbit tracker application"# so basically hum string keh andar curly braces seh space define kar sakte hai jaha par hum  variable paas kar sakte hai jine value hamene useh jagha par print karni ho 
print(string_template.format(user_name))# so basically format() keh function hai jiske through hum unhe empty braces meh variables koh paas kar sakte hai basically format function meh hum log as arguments paas karenge joh joh variable koh hame string meh use karna hoga
list_1 = [ "apple","mango","banana","watermalon"]  
string_from_list = "/".join(list_1)
print(string_from_list)
print(len(string_from_list))
for a in string_from_list:
    print(a)
print("he said masala chai is \"better\"")# so basically hum ek double quotes keh andar dusra double quote use nahi kar sakte tabhi hame escape sequence use karna padhta hai taki hum double quotes koh skip kar sake 
print(r"this is the best \n tea i can ever had ")
print(r"C:\user\name\piyush\\") # so when working with windows or linux we have to use the  \ to define the path but we know \ is the escape sequence for the "" so isko overcome karne keh liye hame r"" raw string use karni padhti hai  
#*** agar end of the r string meh " seh pehle hamare paas \ hai toh yeh r keh format koh bhi kharab kardega to overcome this hame ek aur forward \ use karna padega
print("apple " in string_from_list)


