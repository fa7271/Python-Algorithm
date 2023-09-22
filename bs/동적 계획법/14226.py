# import sys
#
# sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


# S = int(input())
# dp = [1e9] * 1001
# dp[1] = 0
# dp[2] = 2
# dp[3] = min(dp[2]+2, dp[4]-1)
#
# for i in range(3, 1000):
#     if i % 2 ==0: # 나누어 떨어질때
#         dp[i] = min(dp[i//2] +1, dp[i+1]-1)
#     else:
#         for j in range(1,i): # i = 5 j = 1 ~ 4
#             dp[i] = min(dp[i],dp[j]+dp[i-j+1])
# print(dp[S])


# from collections import deque
#
# s = int(input())
#
# dp = [[-1]*(1001) for _ in range(1001)]
# dp[1][0] = 0
# #화면의 이모티콘, 클립보드 이모티콘
# q = deque([(1, 0)])
#
# while q:
#     screen, clip = q.popleft()
#     if screen == s:
#         print(dp[s][clip])
#         break
#
#     if dp[screen][screen] == -1:
#         dp[screen][screen] = dp[screen][clip]+1
#         q.append((screen, screen))
#
#     if 2 <= screen+clip <= 1000 and dp[screen+clip][clip] == -1:
#         dp[screen+clip][clip] = dp[screen][clip]+1
#         q.append((screen+clip, clip))
#
#
#     if 2 <= screen-1 <= 1000 and dp[screen-1][clip] == -1:
#         dp[screen-1][clip] = dp[screen][clip]+1
#         q.append((screen-1, clip))
#
# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 3. 화면에 있는 이모티콘 중 하나를 삭제한다.

import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque, defaultdict

s= int(input())
dic = defaultdict(int)
dic[(1,0)] = 0
Q = deque([(1,0)])

while Q :
    # 스크린, 클립 뽑아줌
    screen, clip = Q.popleft()
    if screen == s:
        print(dic[(screen,clip)])
        break
    # 3가지 경우
    for d_screnn, d_clip in [(screen,screen),(screen+clip,clip),(screen-1,clip)]:
        # 범위에 들어있을경우
        if 0 <= screen <= 2000 and 0 <=clip <=2000:
            if (d_screnn,d_clip) not in dic.keys():
                dic[(d_screnn,d_clip)] = dic[(screen,clip)]+1
                Q.append((d_screnn,d_clip))

