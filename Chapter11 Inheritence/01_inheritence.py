class Employee:
    company="ITC"
    name="vineet"
    
    def show(self):
        print(f"The name of the Employee is {self.name}  and the company is {self.company}")
        
class Programmer(Employee):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
        
a=Employee()
b=Programmer()
print(a.company,b.company)