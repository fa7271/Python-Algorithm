
# 괄호 문제
from Python.bs.data_structure.Doubly_Linked_Lists import DoublyLinkedList


class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)
    return tokens

def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }
    opStack = ArrayStack()
    postfixList = []
    for i in tokenList:
        if type(i) == int:
            postfixList.append(i)
        elif i == '(':
            opStack.push(i)
        elif i == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        elif i in prec :
            if opStack.isEmpty():
                opStack.push(i)
            else:
                while opStack.size() > 0:
                    if prec[opStack.peek()] >= prec[i]:
                        postfixList.append(opStack.pop())
                    else:
                        break
                opStack.push(i)
        else:
            postfixList += i
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList

def postfixEval(tokenList):
    num = ArrayStack()
    for i in tokenList:
        if type(i) == int:
            num.push(i)
        else:
            A = str(num.pop())
            B = str(num.pop())
            num.push(eval(B+i+A))
    return num.pop()
# eval(my_string)
def solution2(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
# print(solution2("(1 + 2) * (3 + 4)"))
# print(solution2("7 * (9 - (3+2))"))
print(solution2("9/3+(10-8)"))

def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in'({[':
            S.push(c)
        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t!= match[c]:
                    return False
    return S.isEmpty()
def solution1(S):
    answer = ''
    opstact = ArrayStack()

    prec = {
        '*': 3, '/': 3,
        '+': 2, '-': 2,
        '(': 1
    }
    for i in S:
        if i == '(':
            opstact.push(i)
        elif i == ')':
            while opstact.peek() != '(':
                answer += opstact.pop()
            opstact.pop()
        elif i in prec :
            if opstact.isEmpty():
                opstact.push(i)
            else:
                while opstact.size() > 0:
                    if prec[opstact.peek()] >= prec[i]:
                        answer += opstact.pop()
                    else:
                        break
                opstact.push(i)
        else:
            answer += i
    while not opstact.isEmpty():
        answer += opstact.pop()
    return answer

# print(solution1("A*(B+C)"))

class LinkedListStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data
