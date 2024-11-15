import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
B = list(map(int, sys.stdin.readline().rstrip().split()))

numbers = set(A) & set(B)
if not numbers:
    print(0)
    exit()
res = []
while numbers:
    number = max(numbers)
    res.append(number)

    A_idx = A.index(number)
    B_idx = B.index(number)

    A = A[A_idx + 1:]
    B = B[B_idx + 1:]

    numbers = set(A) & set(B)
print(len(res))
print(*res)