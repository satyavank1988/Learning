

def checkBalanceParenthese(expr):
    stack = []
    print "Expresions: ",expr

    for i in range(0,len(expr)):
        if expr[i] in ['[','{','(','<']:
            stack.append(expr[i])
        elif expr[i] in [']','}',')','>']:
            if len(stack)== 0:
                return "Not Balanced"

            else:
                stack.pop(len(stack)-1)
    if len(stack) == 0:
        return "balanced"
    else:
        return "Not balanced "

#ex = "[{[]]}()[]]}}}}}"
#ex = "{[]{([])}}"
ex="<[]()[]{}>"
print checkBalanceParenthese(ex) 
