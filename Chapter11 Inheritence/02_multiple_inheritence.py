class Employee:
    company="ITC"
    name="vineet"
    
    def show(self):
        print(f"The name of the Employee is {self.name}  and the company is {self.company}")
    
    
class coder:
    language="python"
    
    def printlanguages(self):
        print(f"out of all the laguage here is your language: {self.language}")
        
class Programmer(Employee, coder):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
        
a=Employee()
b=Programmer()
b.show()
b.printlanguages()
b.showLanguage()