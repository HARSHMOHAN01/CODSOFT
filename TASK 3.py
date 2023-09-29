#TASK 3
import random
a=int(input("enter the number between 3 to 6 :"))
if a==3:
    b=random.randint(100,999)
    print("YOUR THREE DIGIT SYSTEM GENERATED PASSWORD IS : ",b)
elif a==4:
    b=random.randint(1000,9999)
    print("YOUR FOUR DIGIT SYSTEM GENERATED NUMBER IS : ",b)
elif a==5:
    b=random.randint(10000,99999)
    print("YOUR FOUR DIGIT SYSTEM GENERATED NUMBER IS : ",b)
elif a==6:
    b=random.randint(100000,999999)
    print("YOUR FOUR DIGIT SYSTEM GENERATED NUMBER IS : ",b)
else:
    print("YOU HAVE ENTERED A NUMBER THAT IS OUT OF RANGE")
