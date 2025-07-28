class Employee:
    language="Python" #This is class attribute
    salary=1200000
    
    
    def __init__(self,name,salary,language): #dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
    
    

harry=Employee("vineet",1300000,"c++")
print(harry.name,harry.salary,harry.language)


