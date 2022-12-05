import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
number = list(map(int,input().split()))
op = list(map(int,input().split()))
max_res, min_res = -sys.maxsize -1, sys.maxsize

def solution(num,idx,a,b,c,d):
    global max_res,min_res

    if idx == N:
        max_res = max(max_res, num)
        min_res = min(min_res, num)
    if a > 0:
        solution(num + number[idx], idx+1, a-1, b, c, d)
    if b > 0:
        solution(num - number[idx], idx+1, a, b-1, c, d)
    if c > 0:
        solution(num * number[idx], idx+1, a, b, c-1, d)
    if d > 0:
        solution(int(num / number[idx]), idx+1, a, b, c, d-1)


solution(number[0], 1,op[0], op[1], op[2], op[3])
print(max_res,min_res, sep='\n')





