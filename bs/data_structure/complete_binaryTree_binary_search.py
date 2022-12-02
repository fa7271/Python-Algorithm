class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if self.key == key:
            raise KeyError

        if key < self.key: # 넘어온 키가 작으면서
            if self.left: # 만약에 왼쪽에 있으면
                self.left.insert(key,data) # 한 번더 내려감
            #존재 하지않으면
            else:
                self.left = Node(key,data)

        elif key >self.key:
            if self.right:
                self.right.insert(key,data)
            else:
                self.right = Node(key,data)

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0