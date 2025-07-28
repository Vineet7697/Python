marks1=int(input("Enter the marks 1:"))
marks2=int(input("Enter the marks 2:"))
marks3=int(input("Enter the marks 3:"))

Total_percentage=(100*(marks1+marks2+marks3))/300

if (Total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass:",Total_percentage)
else:
    print("you failed, try again next year!")