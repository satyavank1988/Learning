

def matched(str):
    opn = []
    cls = []
    for i in range(0,len(str)):
        l = str[i]
        if l == "(":
            opn = opn + ["("]
        else:
            if l == ")":
                cls = cls + [")"]
#            else:
#                return (opn,cls)
    if len(opn) == len(cls):
        return True
    else:
        return False
#str1 = "(())))((()))"

def check(str1):
    opn = []
    cls = []
    if len(str1) % 2 != 0:
        return False

    for i in range(0,len(str1)):
        if i in ['(','[','{','<']:
            opn = opn + [i]
        else:
            if i in [')',']','}','>']:
                cls = cls + [i]
    if len(opn) == len(cls):
        return "Parentheses are balanced"
    else:
        return "Parenthese are not balanced"

def isBalanced(expr):
    if len(expr) % 2 != 0:
        return "False! parentheses are Not balanced"
    opening  = set('({[<')
    match = set([('(',')'),('[',']'),('{','}'),('<','>')])
    stack = []
    for char in expr:
        if char in opening:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            lastOpen = stack.pop()
            if (lastOpen, char) not in match:
                return False
    return len(stack) == 0

expr = raw_input("Enter Expr :  ")
#expr = "{}<>[[]][[]]{((<>))}<>(){}"
print isBalanced(expr)




str2 = "{{}<>>[[]]{((<<>))}<>(){}"

#print check(str2)


#print matched(str1)

