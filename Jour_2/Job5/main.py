def calcule(num1,operator,num2):
    if  operator == "+":
        result=num1+num2
    elif operator == "-":
        result=num1-num2
    elif operator == "*":
        result=num1*num2
    elif operator == "/":
        result=num1/num2
    elif operator == "%":
        result=num1%num2
    return result

print(calcule(10,"+",3))
print(calcule(10,"-",3))
print(calcule(10,"*",3))
print(calcule(10,"/",3))
print(calcule(10,"%",3))

    



