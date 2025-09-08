import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def func(A,B,C):
    if B == 1:
        print('s',A%C,B)
        return A % C
    else:
        half = func(A, B//2, C)
        print(B)
        if B % 2 == 0: # 짝수면
            return half * half % C
        else:
            return half * half * A % C




A,B,C =map(int,(input().split()))
print(func(A,B,C))



