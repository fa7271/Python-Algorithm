import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


# N = sys.stdin.readline()
# arr = list(map(int, sys.stdin.readline().split()))
#
# N2 = sys.stdin.readline()
# arr2 =list(map(int, sys.stdin.readline().split()))
#
# res = list()
# for i in arr2:
#     if i in arr:
#         res.append(arr.count(i))
#     else:
#         res.append(0)
#
# print(*res)

n = int(input())

arr = list(map(int, input().split()))

dict = dict()
for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1


m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i in dict:
        print(dict[i], end=' ')
    else:
        print(0, end=' ')


