import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n,m = map(int,input().split())
x = sorted(list(map(int,input().split())))
result = []

def bt(num):
    if m == len(result):
        print(*result)
        return
    for i in range(n):
        if x[i] in result:
            continue
        if any(x[i] < num for num in result):
            continue
        result.append(x[i])
        bt(num+1)
        result.pop()
bt(0)


# def backtracking(depth):
#     if depth == M:
#         print(' '.join(map(str,box)))
#         return
#
#     for i in range(N):
#         if numbers[i] in box:
#             continue
#         box.append(numbers[i])
#         backtracking(depth + 1)
#         box.pop()
#
# box = []