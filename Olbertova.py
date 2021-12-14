#!/usr/bin/env python3

def check_value(x,d):
    if isinstance(x,str):
        if x == d:
            x = 1
        else: 
            x = 0
    else:
        x = 0
    return x

def myderive(f,d):
    value=[]
    der_val=[]

    if isinstance(f,int) or isinstance(f,float):
        der = 0
        return der
    elif isinstance(f,str):
        if (f == d):
            der = 1
        else:
            der = 0
        return der
    
    else:
        for item in f:
            if isinstance(item, str):
                if item=='+' or item=='-' or item=='*' or item=='/':
                    symb=item
                else:
                    value.append(item)
            else:
                value.append(item)
        
        der_val.append(check_value(value[0],d))
        der_val.append(check_value(value[1],d))

        if symb == '+':
            return der_val[0] + der_val[1]
        elif symb == '-':
            return  der_val[0] - der_val[1]
        elif symb == '*':
            # der = (value[0] * der_val[1]) + (der_val[0] * value[1])
            print("['+'","['*',",der_val[0],",",value[1],"]","['*',",value[0],",",der_val[1],"]","]")
        else:
            # der = ((der_val[0] * value[1]) - (value[0] * der_val[1])) / (value[1] * value[1])
            print("['/'","['-'","['*',",der_val[0],",",value[1],"]","['*',",value[0],",",der_val[1],"]","]",",","['*',",value[1],",",value[1],"]]")   





