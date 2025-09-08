import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,input().split())

# while n > 0:
#     if m %2 :
#         m -= 1
#     else:
#         m = m //2
#     if m < 1 or (m == 1 and n > 0):
#         print("NO")
#         exit()
#     n -= 1
# print("YES" if m == 1 else "NO")
#
# 조각의 개수는 (rowCut + 1) * (colCut + 1)

# 대칭적이기 때문에 n까지 안 해도 됨
left = 0 ; right = n // 2
while left <= right:
    x = (left + right) // 2
    y = n - x
    answer= (x+1) * (y+1)
    # 1, 3
    if answer == m :
        print("YES")
        exit()
    #조각이 더 많음
    if answer < m:
        left = x + 1
    else:
        right = x - 1
print("NO")



