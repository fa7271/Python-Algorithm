import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
#
# N, M = map(int,sys.stdin.readline().rstrip().split(" "))
# lst = sorted([int(input()) for i in range(N)])
# start = 0; end = lst[-1]
# while start <= end:
#     mid = (start+end) // 2
#
#     temp =sum(i//mid for i in lst)
#     if temp >= M:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(sum(lst) - M * end)


import sys

N, M = map(int,sys.stdin.readline().rstrip().split(" "))
lst = sorted([int(input()) for i in range(N)])
start = 1; end = lst[0]
while start <= end:
    mid = (start+end) // 2
    print(start,end)
    temp = sum(i//mid for i in lst)
    if temp >= M:
        start = mid + 1
    else:
        end = mid - 1
print(sum(lst) - end * M)







