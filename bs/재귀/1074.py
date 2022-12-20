import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def func(n,r,c):
    if n == 1:
        return 2 * r + c
    half = (2**n)//2
    if r < half and c < half: # 1사분면
        return func(n-1, r, c)
    elif r < half and c >= half:
        return half * half + func(n-1, r, c-half)
    elif r >= half & c < half:
        return 2 * half * half + func(n-1, r-half, c)
    else:
        return 3 * half * half + func(n-1, r-half, c-half)
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
print(func(n, r, c))



