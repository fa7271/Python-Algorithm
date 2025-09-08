import sys
sys.stdin = open('/Python/h.txt', 'r')
input = sys.stdin.readline

#  실패버전
# array = list()
# for i in range(2,10000):
#     count = 0
#
#     for j in range(2,i):
#         if i % j == 0:
#             count += 1
#             break
#     if count == 0:
#         array.append(i)
T=int(input())

array = [False,False] + [True] * 10000
for i in range(2,101):
    if array[i] == True:
        for j in range(i+i, 10001, i):
            array[j] = False
for i in range(T):
    n = int(input())
    a = int(n//2)
    b = a
    while a>0:
        if array[a] and array[b] :
            print(a,b)
            break
        else:
            a -= 1
            b += 1