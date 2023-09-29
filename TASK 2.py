#FUNCTION OF CALCULATOR
def HARSH1():
    A=int(input("ENTER THE FIRST NUMBER THAT YOU WANT : "))
    B=int(input("ENTER THE SECOND NUMBER THAT YOU WANT : "))
    C=input("ENTER THE SYMBOL FOR THE CALCULATION THAT YOU WANT TO DO LIKE +,-,X,/,** : ")
    if C=="+":
        D=A+B
    elif C=="-":
        D=A-B
    elif C=="X":
        D=A*B
    elif C=="/":
        D=A/B
    else:
        D=A**B
    print(D)
HARSH1()
