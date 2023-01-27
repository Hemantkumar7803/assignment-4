# assignment-4
# SOLUTION 1
marks=int(input("enter your marks please"))
if(0=<marks<25):
    print("F grade")
elif(marks>=25 and marks<45):
    print("E grade")
elif(marks>=45 and marks<50):
    print("D grade")
elif(marks>=50 and marks<60):
    print("C grade")
elif(marks>=60 and marks<80):
    print("B grade")
elif(100>=marks>=80):
    print("A grade")
else:
    print("enter valid marks ")
