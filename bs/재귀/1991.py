import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())

tree = {}
for i in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left,right]

def solution(root):
    if root != ".":
        print(root, end="")
        solution(tree[root][0])
        solution(tree[root][1])


def solution2(root):
    if root != ".":
        solution2(tree[root][0])
        print(root, end="")
        solution2(tree[root][1])


def solution3(root):
    if root != ".":
        solution3(tree[root][0])
        solution3(tree[root][1])
        print(root, end="")


solution("A")
print()
solution2("A")
print()
solution3("A")



