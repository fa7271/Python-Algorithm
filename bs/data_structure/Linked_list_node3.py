class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):     #dummy node 를 만들어 줌
        self.nodeCount = 0  # 노드 카운트 0
        self.head = Node(None)  # 첫  헤드 논
        self.tail = None        # 첫  꼬리 논
        self.head.next = self.tail  # 0 이니깐 성립

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:        # curr.next 가 살아 있는한
            curr = curr.next    # curr. next 를 curr 로 하고
            result.append(curr.data)    # 데이터를 추가한다.
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0 # 더미노드 이전에는 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:       # tail 의 뒤에 새로운 노드를 삽입하는 경우
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1: # 둘다 같은 경우는 빈 리스트에 넣는 경우이기 때문에
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def concat(self, L):
        self.tail.next = L.head.next
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

    def popAfter(self, prev):
        # prev가 맨 마지막 노드인 경우를 고려 X
        curr = prev.next
        answer = curr.data

        # 삭제하는 노드가 리스트의 맨 마지막 노드인 경우, tail을 prev로 조정
        if curr.next == None:
            self.tail = prev
            prev.next = None
        # 그 외의 경우
        else:
            prev.next = curr.next

        self.nodeCount -= 1
        curr = None
        return answer

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        else:
            return self.popAfter(self.getAt(pos-1))

