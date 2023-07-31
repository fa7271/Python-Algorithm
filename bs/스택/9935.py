import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

temp = list(input().rstrip())  # 입력 받을 때 개행 문자를 제거합니다.
D = sys.stdin.readline().rstrip()  # 폭발 문자열 D도 개행 문자를 제거합니다.
D_len = len(D)
stk = []
for i in temp:
    stk.append(i)
    if len(stk) >= D_len:
        if "".join(stk[-D_len:]) == D:
            for _ in range(D_len):
                stk.pop()
print("".join(stk) if len(stk) >= 1 else "FRULA")