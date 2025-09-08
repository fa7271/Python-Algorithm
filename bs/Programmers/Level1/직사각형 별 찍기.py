import math
def solution():

    a, b = map(int, input().strip().split(' '))
    print(('*'*a + '\n')*b)

print(solution(5,3))