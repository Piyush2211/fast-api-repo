username = "Piyush Sharma"
def check_clousure ():
    print(username)
print(username)
check_clousure()

global_check_closure =99

def func2(y):
    z = global_check_closure + y
    return z

def func3():
    global global_check_closure 
    global_check_closure = 22 
    return global_check_closure
    # print(global_check_closure)
result= func2(4)
result2 = func3()
print(str(result)+":"+ str(result2)+"this is the global value : "+str(global_check_closure))


x_value_clousure = 99

def f1 ():
    x_value_clousure =88
    def f2():
        print(x_value_clousure)
    return f2
my_result = f1()
my_result()

def out_method(outer_param):
    def inner_method(inner_param):
        return inner_param ** outer_param
    return inner_method

function_tester = out_method(2)
function_tester2 = out_method(3)
print(function_tester(7))
print(function_tester2(8))


