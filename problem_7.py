# Customize a coffee order:"Small","Medium"or large with an option for "Extra Large " short of expresso
user_coffee_size = input("Enter 1 for Small size \n Enter 2 for Medium \n Enter 3 for Large : \n")
coffee_size = "none"
match user_coffee_size:
    case  "1":
     coffee_size="Small"
    case  "2" :
      coffee_size = "Medium"
    case "3":
        coffee_size = "Large"

extra_short = input("Enter ex for extra expresso short: \n").lower()

print("Your order is \n"+coffee_size+"\n"+extra_short)


        
