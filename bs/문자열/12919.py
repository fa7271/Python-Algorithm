
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

str_A = input()
str_B = input()
def solution(x):
    if x == str_A:
        print(1)
        exit(0)
    if len(x) == 1:
        return 0
    if x[-1] == "A":
        solution(x[:-1])
    if x[0] == "B":
        solution(x[1:][::-1])
solution(str_B)
print(0)