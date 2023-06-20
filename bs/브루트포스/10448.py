import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(sys.stdin.readline())


def find(n):
    for i in range(len(t)):
        for j in range(i, len(t)):
            for k in range(j, len(t)):
                if t[i]+t[j]+t[k] == n:
                    return 1
    return 0

t = [1]
for i in range(2,45):
    t.append(t[-1]+i)
for _ in range(T):
    n = int(input())
    print(find(n))

