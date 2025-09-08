import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())  # N은 격자 사이즈, M은 치킨집 개수
graph = []  # 격자 정보를 저장하는 리스트
house = []  # 집의 위치를 저장하는 리스트
chicken = []  # 치킨집의 위치를 저장하는 리스트

# 격자 정보 입력 및 집, 치킨집 위치 저장
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split(" "))))
    for j in range(N):
        if graph[i][j] == 1:  # 집인 경우
            house.append((i, j))
        if graph[i][j] == 2:  # 치킨집인 경우
            chicken.append((i, j))

arr = []  # 선택한 치킨집의 인덱스를 저장하는 리스트
res = int(1e9)  # 결과값을 저장하는 변수 (초기값은 큰 값으로 설정)

def dfs(num, cnt):
    global res
    if num > len(chicken):  # 현재 선택한 치킨집의 개수가 전체 치킨집의 개수를 초과하는 경우
        return
    if cnt == M:  # 목표치인 M개의 치킨집을 선택한 경우
        total = 0  # 현재 조합에 대한 치킨 거리의 총합
        for x, y in house:  # 모든 집에 대해서
            dist = int(1e9)  # 현재 집에서의 최소 치킨 거리 (초기값은 큰 값으로 설정)
            for idx in arr:  # 선택한 치킨집에 대해서
                k, l = chicken[idx]  # 치킨집의 위치
                dist = min(dist, abs(x - k) + abs(y - l))  # 현재 집과의 치킨 거리 갱신
            total += dist  # 치킨 거리를 총합에 더함
        res = min(total, res)  # 현재 조합의 치킨 거리 총합과 이전 최소값을 비교하여 갱신
        return
    arr.append(num)  # 현재 치킨집을 선택한 경우
    dfs(num + 1, cnt + 1)  # 다음 치킨집을 선택하는 경우로 재귀 호출
    arr.pop()  # 선택한 치킨집을 제거하고 다른 치킨집을 선택하는 경우
    dfs(num + 1, cnt)  # 다음 치킨집을 선택하지 않는 경우로 재귀 호출
    return res  # 최종적인 결과값 반환

print(dfs(0, 0))  # 초기 호출
print(dfs(0,0))

# arr = []
# real_check = int(1e9)
# def back(num,cnt):
#     global real_check
#     if num > len(chicken):
#         return
#     if cnt==M:
#         result_tot = 0
#         for hx,hy in house:
#             min_check = int(1e9)
#             for idx in arr:
#                 cx,cy = chicken[idx]
#                 min_check = min(min_check,abs(hx-cx)+abs(hy-cy))
#
#             result_tot += min_check
#
#         real_check = min(result_tot,real_check)
#         return
#     arr.append(num)
#     back(num+1,cnt+1)
#     arr.pop()
#     back(num+1,cnt)
#     return real_check
#
# print(back(0,0))
#

# def dfs():

