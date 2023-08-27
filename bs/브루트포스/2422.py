import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
N, M = map(int,input().split(" "))

lst = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(M)]
number = [i for i in range(1,N+1)]

num_lst = list(combinations(number,3))
res = []
for i in num_lst: # 조합을 하나 꺼내고 2 4 5
    for j in lst: # 만나면 안되는 리스트들을 하나씩 검사한다.
        flag = True
        jj = set(j)
        if len(set(i) & jj) == 2: # 조합이 성공되면
            flag = False
            break
    if flag == True:
        res.append(i)
print(res)

# import sys
# from itertools import combinations
# N, M = map(int,input().split(" "))
# # 그래프를 만들어 각 번호별 만나면 안되느 숫자들 True 로 바꿔줌.
# graph = [[False] * N for _ in range(N)]
# for i in range(M):
#     a,b = map(int,sys.stdin.readline().rstrip().split(" "))
#     graph[a-1][b-1] = True
#     graph[b-1][a-1] = True
#
# res = 0
# for combi in combinations(range(N),3):
#
#     if graph[combi[0]][combi[1]] or graph[combi[0]][combi[2]] or graph[combi[1]][combi[2]]: # 한 개라도 조합에 포함되어 있으면
#         continue # 안됨
#     res += 1 # 다 통과 했으면 되는거임
# print(res)
