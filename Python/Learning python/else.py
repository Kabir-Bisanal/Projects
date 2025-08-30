try:
    a = int(input("Enter the number to divide from :"))
    b = int(input("Enter the numebr to divide by :"))
    c = a/b
    print(c)
except Exception as e:
    print(e)
else:
    print("Program executed")
