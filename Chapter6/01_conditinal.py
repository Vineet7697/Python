a=int(input("Enter ypur age:"))
if(a>=18):
    print("you are eligible for vote")
elif(a<0):
    print("you are entering invalid number")
elif(a==0):
    print("you are entering 0 which is not a valid age")
else:
    print("you are not eligible for vote")
    
print("End of program")