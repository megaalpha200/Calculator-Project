UNARY_OP_ADD = 'UN_ADD'
UNARY_OP_SUB = 'UN_SUB'

ADDITION_OPERATOR = '+'
SUBTRACTION_OPERATOR = '-'
MULTIPLICATION_OPERATOR = "*"
DIVISION_OPERATOR = '/'

MULTIPLY_DIVIDE_PRECEDENCE_LEVEL = 1
ADD_SUBTRACT_PRECEDENCE_LEVEL = 0

UNDEDFINED_RESULT = 'undefined'

VALID_CHARS = '0123456789+-*/'


def solveEquation(equInput):
    return calculateRPNExpression(convertToRPN(equInput))


def calculateRPNExpression(rpnExprList):
    rpnExprTempList = rpnExprList.copy()

    exprStack = []

    for el in rpnExprTempList:
        if isOperator(el):
            secondOp = exprStack.pop()
            firstOp = exprStack.pop()
            exprStack.append(calculate(firstOp, secondOp, el))
        else:
            exprStack.append(el)
    
    return exprStack[0]



def calculate(op1, op2, operator):
    if op1 == UNDEDFINED_RESULT or op2 == UNDEDFINED_RESULT:
        return UNDEDFINED_RESULT
    else:
        if operator == ADDITION_OPERATOR:
            return op1 + op2
        elif operator == SUBTRACTION_OPERATOR:
            return op1 - op2
        elif operator == MULTIPLICATION_OPERATOR:
            return op1 * op2
        elif operator == DIVISION_OPERATOR:
            if (op2 == 0):
                return UNDEDFINED_RESULT
            else:
                return round(op1 / op2)



def convertToRPN(equStr):
    tempEquStr = equStr

    tempOperand = ""
    postfixList = []
    operatorStack = []

    try:
        count = 0
        unaryMode = False
        unaryOP = ""

        for token in tempEquStr:
            if token not in VALID_CHARS:
                raise ValueError
            elif count == 0 and operatorPrecedenceLevel(token) == ADD_SUBTRACT_PRECEDENCE_LEVEL:
                unaryMode = True
                unaryOP = token
            elif isOperator(token) and tempOperand != "":
                if unaryMode and unaryOP == SUBTRACTION_OPERATOR:
                    postfixList.append(int(tempOperand) * -1)
                else:
                    postfixList.append(int(tempOperand))
                    
                unaryMode = False
                unaryOP = ""

                tempOperand = ""
                # print("\n\n******\nAppending operand...\n")
                # print("Postfix List (OP): ")
                # print(postfixList)

                reversedOperatorStack = operatorStack.copy()
                reversedOperatorStack.reverse()
                # print("\nReveresed OP Stack: ")
                # print(reversedOperatorStack)

                for op in reversedOperatorStack:
                    if hasLowerOrEqualPrecedence(token, op):
                        postfixList.append(operatorStack.pop())
                        # print("\nAppending operator...\n")
                        # print("Postfix List (LEP): ")
                        # print(postfixList)
                        # print(reversedOperatorStack)

                operatorStack.append(token)
                # print("\nOperator Stack: ")
                # print(operatorStack)
                # print("\n******")
            else:
                tempOperand = tempOperand + token
            
            count = count + 1

        
        if unaryMode and unaryOP == SUBTRACTION_OPERATOR:
            postfixList.append(int(tempOperand) * -1)
        else:
            postfixList.append(int(tempOperand))
        tempOperand = ""
        # print("\n\n******\nAppending operand...\n")
        # print("Postfix List (END): ")
        # print(postfixList)
        # print("\n******")

        while len(operatorStack) != 0:
            postfixList.append(operatorStack.pop())
    except ValueError:
        postfixList.clear()
        postfixList.append(UNDEDFINED_RESULT)
    finally:
        # print(postfixList)
        return postfixList


def isOperator(op):
    if op == ADDITION_OPERATOR or op == SUBTRACTION_OPERATOR or op == MULTIPLICATION_OPERATOR or op == DIVISION_OPERATOR:
        return True
    else:
        return False


def hasLowerOrEqualPrecedence(op1, op2):
    op1PrecedenceLevel = operatorPrecedenceLevel(op1)
    op2PrecedenceLevel = operatorPrecedenceLevel(op2)

    # print("\n")
    # print(op1PrecedenceLevel <= op2PrecedenceLevel)
    return op1PrecedenceLevel <= op2PrecedenceLevel


def operatorPrecedenceLevel(op):
    if op == MULTIPLICATION_OPERATOR or op == DIVISION_OPERATOR:
        return MULTIPLY_DIVIDE_PRECEDENCE_LEVEL
    elif op == ADDITION_OPERATOR or op == SUBTRACTION_OPERATOR:
        return ADD_SUBTRACT_PRECEDENCE_LEVEL


def main():
    while True:
        raw_equ = input("Please enter an equation and I will provide an answer (or enter 'quit' to exit):\n")
        equ = raw_equ.replace(" ", "")
        
        if equ == 'quit':
            print("\n\nQuitting...")
            exit(0)
        else:
            print(solveEquation(equ))

    
main()
