def basic_op(operator, value1, value2):
    #your code here
    if (operator == '+'):
        sum=value1+value2
        return sum
    elif(operator=='-'):
        diff=value1-value2
        return diff
    elif(operator=='*'):
        mul=value1*value2
        return mul
    elif(operator=='/'):
        div=value1//value2
        return div
        
def arithmetic(a, b, operator):
    #your code here
    if(operator=='add'):
        return a+b
    elif(operator=='subtract'):
        return a-b
    elif(operator=='multiply'):
        return a*b
    elif(operator=='divide'):
        return a/b
