def logger(func):
    def wrapper():
        print("calling function")
        func()
        print("Function Executed")
    return wrapper
    

def enter_two_numbers():
    a = int(input("enter the first number"))
    b = int(input("enter the second number"))
    result = add_two_numbers(a,b)
    print("Result:",result)
    return a, b
def add_two_numbers(a,b):
    return a+ b
a = logger(enter_two_numbers)
a()
    
   
