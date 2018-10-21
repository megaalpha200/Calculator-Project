NEGATION_SIGN = 'n'

def solveEquation(equ):
    equStack = []

    result = 0

    if equ[0] == '-':
        operand = equ[1:]
        equStack.append(int(operand))
        equStack.append(NEGATION_SIGN)
    else:
        count = 0
        for i in equ:
            if isOperator(i):
                firstOp = equ[0:count]
                secondOp = equ[count+1:]

                equStack.append(int(secondOp))
                equStack.append(int(firstOp))
                equStack.append(i)
                
            count += 1


    result = calculate(equStack)
    equStack.clear()
    return result

def isOperator(op):
    if op == '+' or op == '-' or op == '*' or op == '/':
        return True
    else:
        return False

def calculate(stack):
    tempStack = stack

    temp = tempStack.pop()
    
    if (temp == NEGATION_SIGN):
        operand = tempStack.pop()
        return (operand * -1)
    else:
        firstOp = tempStack.pop()
        secondOp = tempStack.pop()

        if temp == '+':
            return (firstOp + secondOp)
        elif temp == '-':
            return (firstOp - secondOp)
        elif temp == '*':
            return (firstOp * secondOp)
        elif temp == '/':
            if (secondOp == 0):
                return 'undefined'
            else:
                return (firstOp / secondOp)

def main():
    while(True):
        equ = input("Please enter an equation and I will provide an answer (or enter 'quit' to exit):\n")    
        
        if(equ == 'quit'):
            print("\n\nQuitting...")
            exit(0)
        else:
            print(solveEquation(equ))

    
main()