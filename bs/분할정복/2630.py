import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


# def check(x, y, n, arr):
#     # 탈출 조건
#     if n == 1:
#         if arr[x][y] == 1:
#             return [0, 1] # 1 카운트 증가
#         else:
#             return[1, 0] # 0카운트 증가
#     left_up = check(x, y, n//2, arr) # 2사분면 체크
#     right_up = check(x, y+n//2, n//2, arr) # 1사분면 체크
#     left_down = check(x+n//2, y, n//2, arr) # 3사분면 체크
#     right_down = check(x+n//2, y+n//2, n//2, arr) #4사분면 체크
#
#     # 각 축소 후 압축할지 여부 결정
#     if left_up == right_up == left_down == right_down ==[0,1] or left_up == right_up == left_down == right_down == [1,0]:
#         return left_up # 4개가 같은 숫자면 1개로 리턴
#     else:
#         return list(map(sum, zip(left_up, right_up, left_down, right_down)))
#
#
# def solution(arr):
#     answer = check(0, 0, len(arr), arr)
#     for i in answer:
#         print(i)

def solution(x,y,N):
    global res
    color = arr[x][y]
    for i in range(x,x+N):
        for j in range(y, y+N):
            if color != arr[i][j]:
                solution(x, y, N//2)
                solution(x+N//2, y, N//2)
                solution(x,y-N//2, N//2)
                solution(x+N//2, y-N//2, N//2)
                return
    if color == 1:
        res[1] += 1
    else:
        res[0] +=1

res = [0,0]
N = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for i in range(N)]
solution(0,0,N)
print(res)