import logging
values = [1,2,3,4,5,6,7,8,9,"Hello",0]
try:
 for value in values:
    print(10/int(value))
except ValueError as e:
   print("Error occured ! :"+str(e))    
except ZeroDivisionError as e:
    print("Error occured ! Division failed: "+str(e))
except Exception as e:
   logging.exception(e)
print("Hello")    