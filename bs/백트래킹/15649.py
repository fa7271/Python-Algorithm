import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# input = sys.stdin.readline
# # input = int(sys.stdin.readline())
#
# n, m = map(int, input().split())
# s = []
#
# def f():
#     if len(s) == m:
#         print(*s)
#         return
#
#     for i in range(1, n + 1):
#         if i in s:
#             continue
#         s.append(i)
#         f()K
#         s.pop()
# f()

n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)                   # 인덱스 1부터 바로 접근하기 위해서 >> 편리
result = []

def solve(num):
    if num == m:                            # 탈출 조건 깊이와 m 이 같을떄
        return
    for i in range(1,n+1):
        if visited[i] == False:             # 방문 하지 않은곳이라면
            visited[i] = True               # 방문여부 체크해줌 방문했으면 True 로 바꿔줌
            result.append(i)                # result 결과 리스트 값 추가
            solve(num+1)                    # 다음꺼 재귀 호출
            print(result)
            visited[i] = False              # False 로 해주지 않으면 그 다음꺼 탐색 불가능
            result.pop()                    # 마지막꺼 나오니까 pop으로 빼내줌


solve(0)

# from itertools import permutations
#
# N,M = map(int,input().split())
#
# P = permutations(range(1,N+1),M)
#
# for i in P:
#     print(" ". join(map(str,i)))


# 시간복잡도 중복이 가능하면 O(N^2) (10개 까지 가능)   중복불가 > O(N!) (8개까지 가능)