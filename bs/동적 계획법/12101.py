import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int, input().split(" "))

res = []
count = 0


def bt(sum, res):
    global count
    if sum > n:
        return
    if n == sum:
        count += 1
        if count == k:
            print("+".join(res))
            exit()
    for i in [1, 2, 3]:
        res.append(str(i))
        bt(sum + i, res)
        res.pop()


bt(0, [])
print(-1)