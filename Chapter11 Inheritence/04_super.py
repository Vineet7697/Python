class Employee:
    def __init__(self):
        print("constructor of Employee")
    a=1
    
class programmer(Employee):
    def __init__(self):
      super().__init__()  #call the parent constructor (ex-constructor of Employee)
      print("constructor of programmer")
    b=2
    
class manager(programmer):
    
    def __init__(self):
        super().__init__() #call the parent constructor (ex-constructor of programmer)
        print("constructor manager")
    c=3
o=manager()
print(o.a,o.b,o.c)