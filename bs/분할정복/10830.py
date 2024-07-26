import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]


def solution(arr, M):
    if M == 1:  # 1 곱할때는 그냥 리턴
        return arr

    ar = solution(arr, M // 2)
    cal = []
    for i in range(N):
        result = []
        for l in range(N):
            a = 0
            for j in range(N):
                a += ar[i][j] * ar[j][l]
            result.append(a % 1000)
        cal.append(result)

    answer = []
    if M % 2 == 1:
        for i in range(N):
            result = []
            for l in range(N):
                a = 0
                for j in range(N):
                    a += cal[i][j] * arr[j][l]
                result.append(a % 1000)
            answer.append(result)
    else:
        answer = cal
    return answer


for i in solution(arr, M):
    for j in i:
        print(j, end=" ")
    print()


def 행렬곱셈(A, B, n):
    maps = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                maps[i][j] += (A[k][i] + B[k][j])
            maps[i][j] % 1000
    return maps
