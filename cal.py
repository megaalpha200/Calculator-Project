def solveEquation(equ):
    equStack = []

    result = 0

    count = 0
    for i in equ:
        if i == '+':
            firstOp = equ[0:count]
            secondOp = equ[count+1:]
            equStack.append(int(secondOp))
            equStack.append(int(firstOp))
            equStack.append('+')
            result += calculate(equStack)
            equStack.clear()
        count += 1

    return result

def calculate(stack):
    tempStack = stack

    temp = tempStack.pop()
    if temp == '+':
        firstOp = tempStack.pop()
        secondOp = tempStack.pop()
        return (firstOp + secondOp)

def main():
    equ = input("Please enter an equation and I will provide an answer:\n")    
    print(solveEquation(equ))
    
main()