import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k, q = map(int, sys.stdin.readline().rstrip().split())


# 부모 노드로 이동
def find(x):
    return (x - 2) // k + 1


def unionfind(a, b):
    distance = 0
    # 숫자가 클수록 뒤에임
    while a != b:
        # 부모로 바꿔줌
        if a > b:
            a = find(a)
        else:
            b = find(b)
        distance += 1
    return distance


for _ in range(q):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if k == 1:
        print(abs(a - b))
    else:
        print(unionfind(a, b))
