import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = list(input())

res = -1e9


def solution(temp, idx):
    global res
    # 계산 다 했으면
    if idx == n:
        res = max(res, int(temp))
        return
    # 뒤에 괄호를 치는경우
    if idx + 4 <= n:
        solution(str(eval(''.join([temp, lst[idx]] + [str(eval(''.join(lst[idx + 1:idx + 4])))]))), idx + 4)
    solution(str(eval(''.join([temp] + lst[idx:idx + 2]))), idx + 2)


solution(lst[0], 1)
print(res)
