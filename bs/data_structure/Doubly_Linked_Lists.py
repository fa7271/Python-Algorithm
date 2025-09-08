class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None) # head dummy node
        self.tail = Node(None) # tail dummy node
        self.head.prev = None
        self.head.next = self.tail # 진행 방향 >>
        self.tail.prev = self.head # 진행 방향 <<
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next: # next 두번 쓴 이유: 빈 노드일때 next 면 tail 을 가르킴
            curr = curr.next
            result.append(curr.data)
        return result
    def reverse(self):
        result = []
        curr =self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2: # 뒤쪽이면 뒤에서부터 찾아옴
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        prev.next = curr.next
        curr.next.prev = prev
        curr.next = None
        curr.prev = None
        self.nodeCount -=1
        return curr.data


    def popBefore(self, next):
        curr = next.prev
        curr.prev.next = next
        next.prev = curr.prev
        curr.next = None
        curr.prev = None
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        else:
            return self.popAfter(self.getAt(pos-1))
    def concat(self, L):
        self.tail.prev.next, L.head.next.prev = L.head.next, self.tail.prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount

def solution(x):
    return 0