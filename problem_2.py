# Movie Tickets are priced based on age : $12 for adults (18 and over),$8 for children . Everyone gets a $2 discount on wednesday
from datetime import datetime
current_date = datetime.now()
weekday_number = current_date.weekday()
print(weekday_number)

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

today_day =days[weekday_number]

user_age= int(input("Please enter your age : \n"))

def ticket_price( buyer_age,today_day):
    
    ticket_price_value  = 0
    if 0 > buyer_age:
        print("plese enter a valid age ")
        return None
     
    if 0 < buyer_age <18:
       ticket_price_value = ticket_price_value + 8
    elif 18 <= buyer_age:
        ticket_price_value = ticket_price_value + 12
    
    if  today_day=="Wednesday":
        ticket_price_value = ticket_price_value -2
        
    # print(str(ticket_price_value)+" "+str(buyer_age)+" " +(today_day)+"ticket_price_value")

    return ticket_price_value


ticket_price_value = ticket_price(user_age,today_day)

print("price of the ticket is :\n" + str(ticket_price_value))

