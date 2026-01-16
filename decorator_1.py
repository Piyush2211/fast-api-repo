import time

def timer(func):
     def wrapper(*args,**kwargs):
          start_time = time.time()
          result = func(*args,**kwargs)
          end_time = time.time()
          print(f"{func.__name__}  has ran in {end_time -start_time} time")
          return result
     return wrapper  

def running_func(func):
     def wrapper(*args,**kwargs):
          result = f"{func.__name__} is the function that was running "
          return result
     return wrapper      
@timer 
def example_func(n):
     time.sleep(n)

@running_func
def example_func_2():
     print("this is the example function 2")

example_func(5)

print(example_func_2())