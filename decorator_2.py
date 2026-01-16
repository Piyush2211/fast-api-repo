# Create a decorator to print the function name and the values of its arguments every time the function is called 

def where_from(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        args_value = ", ".join(str(arg) for arg in args)# basically yaha par hamre pass ek tuple hai joh join ,keh sath ek string meh convert karke dega join jisko humne str(arg) for agr in args seh convert kara hai  
        kwargs_value = ", ".join( f"{key}={value}"for key , value in kwargs.items()) #basically yaha par hamre pass ek dictonary hai joh join ,keh sath ek string meh convert karke dega join jisko humne f"{key}={value}"for key , value in kwargs.items() 
 
        print( f"{func.__name__} , {args_value} , {kwargs_value}")
        return None
    return wrapper

@where_from
def greet(name,greeting= "Welcome"):
    print(f"{greeting }, {name} this is the python decorator ")

greet("Piyush","Hi welocome !!!")    