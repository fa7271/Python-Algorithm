import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')


# M,N = input().split()
# M = int(M)
# N = int(N)
# for i in range(M,N+1):  #3부터 16까지
#     if i != 1:
#         for k in range(2,i):
#             if i % k ==0:
#                 break
#         else:
#             print(i)
#       답은 나오지만 시간초과 빅오 O(n^2)

M,N = input().split()
M = int(M)
N = int(N)
for i in range(M,N+1):
    if i == 1:
        continue
    for j in range(2,int(i**(1/2))+1):
        if i % j == 0:
            break
    else: print(i)

# 제곱근을 사용해 시간초과를 막음





