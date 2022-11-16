# from doublylinkedlist import Node
# from doublylinkedlist import DoublyLinkedList

# 괄호 문제

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

print(solution1("A*(B+C)"))
# print(solution("[(A + B) * C]"))

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
