import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def func(n,r,c,k):
    if n == 1:
        return k
    half = (2**n)//2
    if r < half and c < half: # 1사분면
        return func(n-1, r, c, 0)
    elif r < half and c >= half:
        return half * half + func(n-1, r, c-half, 1)
    elif r >= half & c < half:
        return 2 * half * half + func(n-1, r-half, c, 2)
    else:
        return 3 * half * half + func(n-1, r-half, c-half, 3)
# def find_q(n, r, c):
#
#     num = 2**(n-1)
#
#     if (r < num) & (c < num): # 1사분면
#         return 0
#     elif (r < num) & (c >= num): # 2사분면
#         return 1
#     elif (r >= num) & (c < num): # 3사분면
#         return 2
#     else: # 4사분면
#         return 3

n,r,c =map(int,(input().split()))
print(func(n, r, c, 0))



