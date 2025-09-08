import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
n = int(input())


def postorder(graph, tree):
    stk = []
    for i in graph:
        if i == "nil":
            i = 0
        else:
            i = ord(i) - ord("A") + 1
        if i != 0 and len(stk) >= 2:
            right = stk.pop()
            left = stk.pop()
            tree[right] = i
            tree[left] = i
        stk.append(i)
    root = stk[-1]
    tree[root] = root
    return tree


for _ in range(n):
    # end 제거
    A = list(map(str, sys.stdin.readline().rstrip().split()))[:-1]
    B = list(map(str, sys.stdin.readline().rstrip().split()))[:-1]

    AA = [0] * 27
    BB = [0] * 27

    if len(A) in [1, 2] and len(B) in [1, 2]:
        print("true")
        continue
    elif len(A) != len(B):
        print("false")
        continue
    left = postorder(A, AA)
    right = postorder(B, BB)
    res = True
    for left_num, right_num in zip(left[1::], right[1::]):
        if left_num != right_num:
            res = False
            break
    print("true" if res else "false")
