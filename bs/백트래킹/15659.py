import math
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())
numbers = list(map(str, sys.stdin.readline().rstrip().split()))
lst = list(map(int, sys.stdin.readline().rstrip().split()))

start = numbers[0]
max_res = -1e9
min_res = 1e9


def solution(temp, addition, subtraction, multiplication, division, depth):
    global max_res, min_res
    if addition + subtraction + multiplication + division == 0:
        max_res = max(max_res, eval(temp))
        min_res = min(min_res, eval(temp))
    if addition > 0:
        solution(temp + "+" + numbers[depth], addition - 1, subtraction, multiplication, division, depth + 1)
    if subtraction > 0:
        solution(temp + "-" + numbers[depth], addition, subtraction - 1, multiplication, division, depth + 1)
    if multiplication > 0:
        solution(temp + "*" + numbers[depth], addition, subtraction, multiplication - 1, division, depth + 1)
    if division > 0:
        solution(temp + "//" + numbers[depth], addition, subtraction, multiplication, division - 1, depth + 1)


solution(start, lst[0], lst[1], lst[2], lst[3], 1)
print(max_res,min_res,sep='\n')
# print(math.ceil(max_res), math.floor(min_res), sep='\n')
