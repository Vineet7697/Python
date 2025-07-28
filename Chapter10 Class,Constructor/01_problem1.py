# Create a class "programmer" for storing information of few programmers workong at microsoft.

class Programmer:
    company="microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
p=Programmer("Rahul",1200000,486226)
print(p.name,p.salary,p.pin)
r=Programmer("Rohan",1200000,486226)
print(r.name,r.salary,r.pin)