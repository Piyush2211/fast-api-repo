# import this
import time
# Implement a decorator that caches the return values of a function, so that when it is called with the same argument , the cached value is returned instead  of re-executing the function 

def cache(func):# best practice to create a decorator is pehle decorator function banao usme function as parameter paas karo firh  uske andar ek wrapper banao jaha par *args and **kwargs pass karo than uske andar apna parameter wala function call karvao func(*args,**kwargs) keh sath meh  and than usko ek variable seh store karvake return kardo and firh wrapper koh bhi return kardo
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper
        
@cache         
def  test_func(variable_1, variable_2):
    time.sleep(7)
    return variable_1 + variable_2

print(test_func(10,20))
print(test_func(10,20))
print(test_func(20,40))