import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# N = int(input())
# lst = [int(input()) for i in range(N)]
#
# arr = [False] * 2 + [True] * 4000000000
# for i in range(2,int(4000000001**0.5)):
#     for j in range(i,4000000001,i):
#         if arr[j] == True:
#             arr[j] = False
#
# for i in range(N):
#     x = int(input())
#     while True:
#         if arr[x] == False:
#             x += 1
#         else:
#             print(x)
#             break
#
N = int(input())

def check(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(N):
    n = int(input())
    while True:
        if n == 0 or n == 1:
            print(2)
            break
        if check(n):
            print(n)
            break
        else:
            n += 1
