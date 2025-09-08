import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

temp =list(input())
N = len(temp)

res = []
for i in range(1,N-1):
    for j in range(i+1,N):
        A = temp[:i]
        B = temp[i:j]
        C = temp[j:]

        A.reverse(); B.reverse(); C.reverse()

        res.append("".join(A+B+C))
res.sort()
print(res[0])