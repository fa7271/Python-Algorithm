# pos번째 노드 찾기 메소드
def getAt(self, pos):
    if pos <= 0 or pos > self.nodeCount:
        return None

    i = 1
    curr = self.head
    while i < pos:
        curr = curr.next
    i += 1
    return curr
