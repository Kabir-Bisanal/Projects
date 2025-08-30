while True:
    try:
        a = int(input("Enter the number to divide from :"))
        b = int(input("Enter the numebr to divide by :"))
        c = a/b
        print(c)
    except Exception as e:
        print(e)
    finally:
        print("Have a great day") #this lien of code is always executed irrespective if there is an error or there isnt
