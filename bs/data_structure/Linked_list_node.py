class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount +1:
            return False
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount + 1:
                prev = self.tail # prev == tail
            else:
                prev = self.getAt(pos -1 )
            prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode
        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1

        return True

    def traverse(self):
        if not self.head:
            return []
        List = []
        curr = self.head
        while curr is not None:
            List.append(curr.data)
            curr = curr.next

        return List




def solution(x):

    return 0

