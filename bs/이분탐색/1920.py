import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
N = sorted(map(int,input().split()))    # 이분탐색 하려면 정렬된 리스트여야 가
m = int(input())
M = list(map(int,input().split()))

def binary(i, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2              # 중앙 값 = m
    if i == N[m]:                   # i가 중앙에 중앙값이면
        return 1                    # 그대로 리턴
    elif i < N[m]:                  # 작으면
        return binary(i, N, start, m-1) # 큰부분 다 자르고 다시시작
    else:                           # 아니면
        return binary(i, N, m+1, end)   # 작은부분 다 자르고 다시시작

for i in M:
    start = 0
    end = len(N)-1
    print(binary(i, N, start, end)) # 리스트 M 중에 1개씩 가져와서 넘겨줌
# for num in M:				            # arr의 각 원소별로 탐색
#     print(1) if num in N else print(0)	# num이 A 안에 있으면 1, 없으면 0 출력
