import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(sys.stdin.readline())


def find(n):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            for k in range(j, len(lst)):
                if lst[i]+lst[j]+lst[k] == n:
                    return 1
    return 0

lst = [1]
for i in range(2,45):
    lst.append(lst[-1]+i)
for _ in range(T):
    n = int(input())
    print(find(n))

