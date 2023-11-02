import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
A = list(map(int,input().split()))
cal = list(map(int,input().split()))
max_res = int(-1e9)
min_res = int(1e9)

def solution(idx,a,b,c,d,res):
    global min_res, max_res
    if idx == n:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return
    if a >= 1:
        solution(idx+1, a-1, b, c, d, res+A[idx])
    if b >= 1:
        solution(idx+1, a, b-1, c, d, res - A[idx])
    if c >= 1:
        solution(idx+1, a, b, c-1, d, res * A[idx])
    if d >= 1:
        solution(idx+1, a, b, c, d-1, int(res / A[idx]))

solution(1,cal[0],cal[1],cal[2],cal[3],A[0])
print(min_res,max_res,sep="\n")