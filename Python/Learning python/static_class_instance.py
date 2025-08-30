class employee:
    company = "TATA"
    @staticmethod
    def __init__(name,salary):
        company="TATA"
        name=name
        salary=salary
        company=company
        print( f"this nam e is {name} and the salary is {salary}")
    @staticmethod
    def sum(a,b):
        return a+b
    
    @classmethod
    def companyy(cls):
        print(cls.company)

e1=employee("kabir bisanal",80000)
e2=employee("rohan biswas",90000)
print(e2.sum(4,5)) 

e1.companyy()
    