import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
lst = list(map(int,sys.stdin.readline().split(" ")))
res = [-1] * N

dic = dict()
for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] +=1
stk = []

for i in range(N):
    # 스택이 존재하고, 스택 마지막에 있는것의 딕셔너리 갯수가, 현재 숫자의 딕셔너리 갯수보다 작으면
    while stk and dic[lst[stk[-1]]] < dic[lst[i]]:
        idx = stk.pop()
        res[idx] = lst[i]
    stk.append(i)
print(*res)