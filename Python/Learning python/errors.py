# while True:
#     try:
#         a = int(input("Enter the number to divide from :"))
#         b = int(input("Enter the numebr to divide by :"))

#         print(f"{a} divided by {b} = {a/b}")
        
#     except ValueError:
#         print("Please enter a proper value to perform the division operation!!")
#     except ZeroDivisionError:
#         print("You cant divide a number by zero!!")
#     except Exception as e:
#         print("Unknown error occured?!")

age = int(input("Enter your age :"))
if (age <18):
    raise ValueError("You need to leaveee!!")
print(f"You are an {age} year old adult nigga")