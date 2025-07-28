class Employee:
    language="Python" #This is class attribute
    salary=1200000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning")
        
    @staticmethod
    def greet():
        print("Good morning")

harry=Employee()
harry.getInfo() 
# Employee.getInfo(harry)
harry.greet()
harry.greet()

