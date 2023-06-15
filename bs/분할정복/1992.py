import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def check(x, y, n, arr):
    # 탈출 조건
    if n == 1:
        return str(arr[x][y])

    left_up = check(x, y, n//2, arr) # 2사분면 체크
    right_up = check(x, y+n//2, n//2, arr) # 1사분면 체크
    left_down = check(x+n//2, y, n//2, arr) # 3사분면 체크
    right_down = check(x+n//2, y+n//2, n//2, arr) #4사분면 체크
    # 각 축소 후 압축할지 여부 결정

    if left_up == right_up == left_down == right_down and len(left_up) == 1:
        return left_up

    # 그렇지 않다면 4개의 영역을 괄호로 묶어서 반환
    return "(" + left_up + right_up + left_down + right_down + ")"

def solution(arr):
    answer = check(0, 0, N, arr)
    for i in answer:
        print(i,end="")

N =int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().strip())) for i in range(N)]
solution(arr)