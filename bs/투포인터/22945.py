import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
ability = list(map(int,input().split()))

left = 0; right = n-1
res = 0
while left + 1 < right:
    # 인원수는 최대임, 그 다음은 작은 숫자의 포인터를 없애야함 그래야 큰 값으로 바뀌어 그 중 작은 숫자를 고름
    res = max(res, (right-left -1) * min(ability[left],ability[right]))
    if ability[left] < ability[right]:
        left += 1
    else:
        right -= 1
print(res)



# for i in range(n):
#     for j in range(i+1,n):
#         if j - i - 1 < 1:
#             continue
#         res = max(res,(j-i-1) * min(ability[j], ability[i]))

